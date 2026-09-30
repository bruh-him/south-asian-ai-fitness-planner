from pathlib import Path

from src.south_asian_fitness_planner.food_ontology import load_ontology, search


ONTOLOGY = Path(__file__).parents[1] / "data" / "south_asian_food_ontology.csv"


def test_ontology_loads():
    entries = load_ontology(ONTOLOGY)
    assert len(entries) >= 30


def test_alias_resolution():
    entries = load_ontology(ONTOLOGY)
    assert search(entries, "murgh karahi")[0].canonical_name == "Chicken Karahi"
    assert search(entries, "masala dosa")[0].canonical_name == "Masala Dosa"
    assert search(entries, "aam")[0].canonical_name == "Mango"


def test_canonical_names_are_unique():
    entries = load_ontology(ONTOLOGY)
    names = [entry.canonical_name for entry in entries]
    assert len(names) == len(set(names))
