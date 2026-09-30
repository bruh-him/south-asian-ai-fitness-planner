from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FoodEntry:
    canonical_name: str
    aliases: tuple[str, ...]
    region: str
    subregion: str
    cuisine: str
    food_type: str


def load_ontology(path: str | Path) -> list[FoodEntry]:
    entries: list[FoodEntry] = []
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            aliases = tuple(
                alias.strip().casefold()
                for alias in row["aliases"].split(";")
                if alias.strip()
            )
            entries.append(
                FoodEntry(
                    canonical_name=row["canonical_name"],
                    aliases=aliases,
                    region=row["region"],
                    subregion=row["subregion"],
                    cuisine=row["cuisine"],
                    food_type=row["food_type"],
                )
            )
    return entries


def search(entries: list[FoodEntry], query: str) -> list[FoodEntry]:
    q = query.strip().casefold()
    if not q:
        return []
    exact = []
    partial = []
    for entry in entries:
        canonical = entry.canonical_name.casefold()
        if q == canonical or q in entry.aliases:
            exact.append(entry)
        elif q in canonical or any(q in alias for alias in entry.aliases):
            partial.append(entry)
    return exact + partial
