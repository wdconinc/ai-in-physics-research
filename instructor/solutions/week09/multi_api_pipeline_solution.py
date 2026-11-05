"""Week 9 Meeting 2 — Multi-API Pipeline: reference solution (instructor only)

Solution to docs/exercises/week09/multi_api_pipeline_broken.py. The three
planted bugs, in the order pairs usually find them:

  (c) normalize_material(): entry["band_gap"] raises KeyError for metals,
      whose Materials Project entries come back without a band_gap field.
  (a) fetch_star(): a bare except swallows SIMBAD's 429 rate-limit error and
      returns last week's stale cache entry (Betelgeuse, Rigel, Polaris) as
      if it were a fresh query.
  (b) normalize_star(): luminosity is in solar luminosities but is stored in
      L_SI without multiplying by L_SUN_W (Sirius comes out at ~23 W).

Each fix carries a one-sentence comment, as students are asked to write.
test_luminosity_is_in_watts() at the bottom is the "fourth test" for pairs
that finish early: it catches bug (b) without anyone reading the numbers.

Usage:
    python multi_api_pipeline_solution.py            # offline
    python -m pytest multi_api_pipeline_solution.py  # extension test

Requirements:
    pip install tenacity astroquery mp-api diskcache
    MP_API_KEY set in the environment (only needed for --live)
"""

import argparse
import json
import logging
import math
import os
import tempfile
import time
from datetime import datetime, timedelta, timezone

import diskcache
import requests
from tenacity import (before_sleep_log, retry, retry_if_exception,
                      stop_after_attempt, wait_exponential)

log = logging.getLogger("pipeline")

L_SUN_W = 3.828e26        # IAU 2015 nominal solar luminosity [W]
PARSEC_M = 3.0857e16      # one parsec [m]
M_V_SUN = 4.83            # absolute V magnitude of the Sun
CACHE_MAX_AGE_S = 24 * 3600

SIMBAD_URL = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"
MP_URL = "https://api.materialsproject.org/materials/summary/"

STARS = ["Sirius", "Vega", "Arcturus", "Altair", "Proxima Centauri",
         "Betelgeuse", "Rigel", "Polaris"]
MATERIALS = ["mp-149", "mp-66", "mp-1143", "mp-30", "mp-22862", "mp-13"]
MP_FIELDS = ["material_id", "formula_pretty", "is_metal", "band_gap"]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def age_seconds(iso_timestamp):
    then = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return (datetime.now(timezone.utc) - then.replace(tzinfo=timezone.utc)).total_seconds()


# --- Live API clients ---------------------------------------------------------

class LiveSimbad:
    """Thin wrapper around astroquery.simbad (astroquery >= 0.4.8)."""

    def __init__(self):
        from astroquery.simbad import Simbad
        self._simbad = Simbad()
        self._simbad.add_votable_fields("plx_value", "V")

    def query(self, name):
        table = self._simbad.query_object(name)
        if table is None or len(table) == 0:
            raise ValueError(f"Object not found in SIMBAD: {name}")
        row = table[0]
        return {"main_id": str(row["main_id"]),
                "V": float(row["V"]),
                "plx_mas": float(row["plx_value"])}


class LiveMaterialsProject:
    """Thin wrapper around mp-api's summary endpoint."""

    def __init__(self):
        from mp_api.client import MPRester
        self._mpr = MPRester(os.environ["MP_API_KEY"])

    def get_summary(self, material_id):
        doc = self._mpr.materials.summary.search(material_ids=[material_id],
                                                 fields=MP_FIELDS)[0]
        # Fields the API left unset are dropped rather than passed on as None.
        entry = {field: getattr(doc, field, None) for field in MP_FIELDS}
        entry["material_id"] = str(entry["material_id"])
        return {k: v for k, v in entry.items() if v is not None}


# --- Fetching with a local cache ----------------------------------------------

def is_rate_limit(exc):
    return (isinstance(exc, requests.HTTPError)
            and exc.response is not None and exc.response.status_code == 429)


@retry(retry=retry_if_exception(is_rate_limit), stop=stop_after_attempt(3),
       wait=wait_exponential(multiplier=1, min=1, max=8),
       before_sleep=before_sleep_log(log, logging.WARNING), reraise=True)
def query_simbad(simbad, name):
    return simbad.query(name)


def fetch_star(simbad, cache, name):
    """Return SIMBAD's V magnitude and parallax for one star, using the cache."""
    key = f"simbad:{name}"
    cached = cache.get(key)
    if cached is not None and age_seconds(cached["retrieved_at"]) < CACHE_MAX_AGE_S:
        log.info("cache hit   %s", key)
        return cached
    log.info("query       %s", key)
    # The bare except silently served last week's cache on a 429, so retry rate limits with backoff and let every other error propagate.
    row = query_simbad(simbad, name)
    row["retrieved_at"] = now_iso()
    cache.set(key, row)
    return row


def fetch_material(mp, cache, material_id):
    """Return the Materials Project summary entry for one material, using the cache."""
    key = f"mp:{material_id}"
    cached = cache.get(key)
    if cached is not None and age_seconds(cached["retrieved_at"]) < CACHE_MAX_AGE_S:
        log.info("cache hit   %s", key)
        return cached
    log.info("query       %s", key)
    entry = mp.get_summary(material_id)
    entry["retrieved_at"] = now_iso()
    cache.set(key, entry)
    return entry


# --- Normalization to the internal schema -------------------------------------

def normalize_star(name, row):
    """Convert a SIMBAD row to the internal schema (SI units).

    Luminosity is estimated from the V magnitude with no bolometric
    correction, so it is good to a factor of a few for very hot or very
    cool stars.
    """
    distance_pc = 1000.0 / row["plx_mas"]
    abs_mag_v = row["V"] - 5 * math.log10(distance_pc / 10)
    luminosity = 10 ** (-0.4 * (abs_mag_v - M_V_SUN))
    return {
        "name": name,
        "simbad_id": row["main_id"],
        "distance_m": distance_pc * PARSEC_M,
        # The magnitude formula gives L in solar luminosities, so convert to watts before storing it as L_SI.
        "L_SI": luminosity * L_SUN_W,
        "source": "SIMBAD",
        "retrieved_at": row["retrieved_at"],
    }


def normalize_material(entry):
    """Convert a Materials Project summary entry to the internal schema."""
    band_gap = entry.get("band_gap")
    if band_gap is None:
        log.warning("%s: band_gap missing from %s", entry["material_id"], MP_URL)
        # Metals come back without band_gap, so read it with .get() and record 0 eV for metals (None otherwise) instead of crashing.
        band_gap = 0.0 if entry.get("is_metal") else None
    return {
        "material_id": entry["material_id"],
        "formula": entry["formula_pretty"],
        "is_metal": entry["is_metal"],
        "band_gap_eV": band_gap,
        "source": "Materials Project",
        "retrieved_at": entry["retrieved_at"],
    }


# --- Provenance ---------------------------------------------------------------

def write_provenance(path, stars, materials, mode):
    payload = {
        "created_at": now_iso(),
        "mode": mode,
        "endpoints": {"SIMBAD": SIMBAD_URL, "Materials Project": MP_URL},
        "constants": {"L_sun_W": L_SUN_W, "parsec_m": PARSEC_M, "M_V_sun": M_V_SUN},
        "stars": stars,
        "materials": materials,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def run(simbad, mp, cache, out_path, mode):
    stars = [normalize_star(name, fetch_star(simbad, cache, name)) for name in STARS]
    materials = [normalize_material(fetch_material(mp, cache, mid)) for mid in MATERIALS]
    write_provenance(out_path, stars, materials, mode)
    print(f"Wrote {out_path}: {len(stars)} stars, {len(materials)} materials")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--live", action="store_true",
                        help="query the real SIMBAD and Materials Project APIs")
    parser.add_argument("--out", default="provenance.json",
                        help="provenance file to write (default: provenance.json)")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)-7s %(message)s")

    if args.live:
        with diskcache.Cache(".pipeline_cache") as cache:
            run(LiveSimbad(), LiveMaterialsProject(), cache, args.out, "live")
    else:
        with tempfile.TemporaryDirectory(prefix="pipeline_cache_") as tmp:
            with diskcache.Cache(tmp) as cache:
                restore_last_week_cache(cache)
                run(OfflineSimbad(), OfflineMaterialsProject(), cache, args.out, "offline")


# ==============================================================================
# OFFLINE SIMULATION — scaffolding, not part of the bug hunt.
# These stand-ins return data shaped like the live clients above, enforce a
# SIMBAD-style rate limit, and restore the cache left behind by last week's
# run, so every run in class behaves the same with no network or API key.
# There are no planted bugs below this line.
# ==============================================================================

# V magnitude and parallax [mas], close to current SIMBAD values.
SIMBAD_SNAPSHOT = {
    "Sirius":           {"main_id": "* alf CMa", "V": -1.46, "plx_mas": 379.21},
    "Vega":             {"main_id": "* alf Lyr", "V": 0.03, "plx_mas": 130.23},
    "Arcturus":         {"main_id": "* alf Boo", "V": -0.05, "plx_mas": 88.83},
    "Altair":           {"main_id": "* alf Aql", "V": 0.76, "plx_mas": 194.95},
    "Proxima Centauri": {"main_id": "NAME Proxima Centauri", "V": 11.13, "plx_mas": 768.07},
    "Betelgeuse":       {"main_id": "* alf Ori", "V": 0.42, "plx_mas": 6.55},
    "Rigel":            {"main_id": "* bet Ori", "V": 0.13, "plx_mas": 3.78},
    "Polaris":          {"main_id": "* alf UMi", "V": 1.98, "plx_mas": 7.54},
}

# Last week's run used an older catalog for the three most distant stars.
LAST_WEEK_OVERRIDES = {
    "Betelgeuse": {"V": 0.50, "plx_mas": 7.63},
    "Rigel":      {"V": 0.18, "plx_mas": 4.22},
    "Polaris":    {"V": 2.02, "plx_mas": 7.56},
}

# Approximate GGA band gaps [eV]; GGA underestimates experimental gaps.
# Metallic entries come back without a band_gap field.
MP_SNAPSHOT = {
    "mp-149":   {"material_id": "mp-149", "formula_pretty": "Si", "is_metal": False, "band_gap": 0.61},
    "mp-66":    {"material_id": "mp-66", "formula_pretty": "C", "is_metal": False, "band_gap": 4.34},
    "mp-1143":  {"material_id": "mp-1143", "formula_pretty": "Al2O3", "is_metal": False, "band_gap": 5.85},
    "mp-30":    {"material_id": "mp-30", "formula_pretty": "Cu", "is_metal": True},
    "mp-22862": {"material_id": "mp-22862", "formula_pretty": "NaCl", "is_metal": False, "band_gap": 5.00},
    "mp-13":    {"material_id": "mp-13", "formula_pretty": "Fe", "is_metal": True},
}


class OfflineSimbad:
    """Stands in for LiveSimbad; allows at most 5 queries per second, like SIMBAD."""

    MAX_QUERIES = 5
    WINDOW_S = 1.0

    def __init__(self):
        self._recent = []

    def query(self, name):
        now = time.monotonic()
        self._recent = [t for t in self._recent if now - t < self.WINDOW_S]
        if len(self._recent) >= self.MAX_QUERIES:
            response = requests.Response()
            response.status_code = 429
            response.url = SIMBAD_URL
            raise requests.HTTPError("429 Client Error: Too Many Requests for url: "
                                     + SIMBAD_URL, response=response)
        self._recent.append(now)
        time.sleep(0.05)  # network latency
        if name not in SIMBAD_SNAPSHOT:
            raise ValueError(f"Object not found in SIMBAD: {name}")
        return dict(SIMBAD_SNAPSHOT[name])


class OfflineMaterialsProject:
    """Stands in for LiveMaterialsProject."""

    def get_summary(self, material_id):
        time.sleep(0.05)  # network latency
        return dict(MP_SNAPSHOT[material_id])


def restore_last_week_cache(cache):
    """Fill the cache with the SIMBAD rows a run seven days ago would have stored."""
    last_week = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
    for name, row in SIMBAD_SNAPSHOT.items():
        cached = dict(row, **LAST_WEEK_OVERRIDES.get(name, {}))
        cached["retrieved_at"] = last_week
        cache.set(f"simbad:{name}", cached)


# --- Extension: a test that catches bug (b) automatically ----------------------

def test_luminosity_is_in_watts():
    """Sirius A is ~25 L_sun ~ 1e28 W; a value off by 1e26 fails this bound."""
    row = dict(SIMBAD_SNAPSHOT["Sirius"], retrieved_at=now_iso())
    assert 1e27 < normalize_star("Sirius", row)["L_SI"] < 1e29


if __name__ == "__main__":
    main()
