"""Build the Claude-friendly food knowledge pack.

The script deliberately keeps food recognition separate from nutrient composition.
It downloads the sampled USDA release used by the upstream reference project,
extracts a compact CSV locally, and preserves the project-authored South Asian
ontology as a separate file.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw_data"
PACK = ROOT / "claude_project_pack"
SOURCE = RAW / "usda_sampled_5000_foods.json"
OUT = PACK / "02_USDA_5000_COMPACT.csv"
ONTOLOGY = ROOT / "data" / "south_asian_food_ontology.csv"
USDA_URL = (
    "https://github.com/zen-apps/ai-fitness-planner/releases/download/"
    "v1.0.1/usda_sampled_5000_foods.json"
)


def download() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    if SOURCE.exists():
        return
    print(f"Downloading USDA sample → {SOURCE}")
    with urlopen(USDA_URL) as response:  # nosec B310: fixed HTTPS source
        SOURCE.write_bytes(response.read())


def compact() -> int:
    PACK.mkdir(parents=True, exist_ok=True)
    with SOURCE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise TypeError("USDA JSON root must be an object/dictionary.")

    foods = data.get("BrandedFoods", [])
    if not isinstance(foods, list):
        raise TypeError("USDA 'BrandedFoods' must be a list.")

    rows: list[dict[str, object]] = []
    for item in foods:
        if not isinstance(item, dict):
            continue
        nutrition = item.get("nutrition_enhanced") or {}
        per_100g = nutrition.get("per_100g") or {}
        macro = nutrition.get("macro_breakdown") or {}
        rows.append(
            {
                "fdc_id": item.get("fdcId", ""),
                "description": item.get("description", ""),
                "brand_owner": item.get("brandOwner", ""),
                "brand_name": item.get("brandName", ""),
                "food_category": item.get("foodCategory", ""),
                "serving_size": item.get("servingSize", ""),
                "serving_unit": item.get("servingSizeUnit", ""),
                "ingredients": item.get("ingredients", ""),
                "calories_per_100g": per_100g.get("energy_kcal", ""),
                "protein_g_per_100g": per_100g.get("protein_g", ""),
                "carbs_g_per_100g": per_100g.get("carbs_g", ""),
                "fat_g_per_100g": per_100g.get("total_fat_g", ""),
                "primary_macro": macro.get("primary_macro_category", ""),
                "high_protein": macro.get("is_high_protein", ""),
                "nutrition_density": nutrition.get("nutrition_density_score", ""),
            }
        )

    if not rows:
        raise RuntimeError("No valid USDA records were extracted.")

    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    download()
    count = compact()
    print(f"Created {OUT} with {count:,} records.")
    print(f"South Asian ontology: {ONTOLOGY}")


if __name__ == "__main__":
    main()
