"""Intentionally broken multi-API pipeline for Week 8 debugging."""
import json
import time

L_SUN_W = 3.828e26


def fetch_simbad_luminosity(object_name: str):
    try:
        raise RuntimeError("429 rate limit from SIMBAD")
    except:  # BUG 1: swallowed rate-limit (no retry, no signal)
        return {"object": object_name, "luminosity_Lsun": 1.2, "source": "stale-cache"}


def fetch_material_entry(material_id: str):
    if material_id.endswith("metal"):
        return {"material_id": material_id}  # band_gap omitted intentionally by API
    return {"material_id": material_id, "band_gap": 1.9}


def normalize_record(simbad_row, mp_row):
    return {
        "object": simbad_row["object"],
        "L_SI": simbad_row["luminosity_Lsun"],  # BUG 2: unit mismatch, should multiply by L_SUN_W
        "band_gap_eV": mp_row["band_gap"],      # BUG 3: missing .get guard -> KeyError on metals
        "source": {"simbad": simbad_row["source"], "materials": "live"},
    }


def write_provenance(path, records):
    payload = {
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "records": records,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def main():
    simbad = fetch_simbad_luminosity("Betelgeuse")
    mp = fetch_material_entry("mp-149-metal")
    row = normalize_record(simbad, mp)
    write_provenance("provenance_broken.json", [row])
    print("Wrote provenance_broken.json")


if __name__ == "__main__":
    main()
