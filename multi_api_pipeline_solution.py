"""Reference solution for the Week 8 broken multi-API pipeline."""
import json
import time

L_SUN_W = 3.828e26


def fetch_simbad_luminosity(object_name: str, attempts: int = 3):
    last_err = None
    for i in range(attempts):
        try:
            if i < 1:
                raise RuntimeError("429 rate limit from SIMBAD")
            return {"object": object_name, "luminosity_Lsun": 1.2, "source": "live"}
        except RuntimeError as exc:
            last_err = str(exc)
            time.sleep(0.1 * (2 ** i))
    raise RuntimeError(f"SIMBAD request failed after retries: {last_err}")


def fetch_material_entry(material_id: str):
    if material_id.endswith("metal"):
        return {"material_id": material_id}
    return {"material_id": material_id, "band_gap": 1.9}


def normalize_record(simbad_row, mp_row):
    band_gap = mp_row.get("band_gap")
    return {
        "object": simbad_row["object"],
        "L_SI": simbad_row["luminosity_Lsun"] * L_SUN_W,
        "band_gap_eV": band_gap,
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
    write_provenance("provenance_solution.json", [row])
    print("Wrote provenance_solution.json")


if __name__ == "__main__":
    main()
