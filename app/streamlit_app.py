from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from south_asian_fitness_planner.food_ontology import load_ontology, search

st.set_page_config(
    page_title="South Asian AI Fitness Planner",
    page_icon="🇵🇰",
    layout="wide",
)

ONTOLOGY = ROOT / "data" / "south_asian_food_ontology.csv"
entries = load_ontology(ONTOLOGY)

st.title("🇵🇰 🇮🇳 South Asian AI Fitness Planner")
st.caption("Claude Project companion • Pakistani • Indian • South Indian nutrition intelligence")

with st.sidebar:
    st.header("Project modules")
    st.write("🧠 Multi-agent planning")
    st.write("🍛 South Asian food resolution")
    st.write("📚 Food-source provenance")
    st.write("📈 Adaptive coaching")
    st.write("🧪 Independent QA")

    st.divider()
    st.subheader("Food coverage")
    st.metric("Ontology entries", len(entries))

    cuisines = sorted({e.cuisine for e in entries})
    regions = sorted({e.region for e in entries})
    st.write(f"Cuisines: {len(cuisines)}")
    st.write(f"Regions: {len(regions)}")

overview, foods, sources = st.tabs(["Overview", "Food Explorer", "Data & Attribution"])

with overview:
    c1, c2, c3 = st.columns(3)
    c1.metric("Planning architecture", "Multi-agent")
    c2.metric("Regional nutrition", "Pakistan + India")
    c3.metric("Planning mode", "Claude Project")

    st.markdown("### Workflow")
    st.code(
        "PROFILE → ENERGY → FOOD SOURCES → MEALS → TRAINING → "
        "COORDINATION → QA → FINAL PLAN → ADAPTATION",
        language="text",
    )

    st.markdown("### Design principle")
    st.info(
        "Recognize South Asian foods first, then select an appropriate composition source. "
        "The ontology is not itself a nutrition database."
    )

with foods:
    st.subheader("South Asian Food Explorer")
    query = st.text_input("Search food / dish / alias", placeholder="e.g. murgh karahi, dosa, aam")
    region_filter = st.selectbox("Region", ["All"] + sorted({e.region for e in entries}))
    cuisine_filter = st.selectbox("Cuisine", ["All"] + sorted({e.cuisine for e in entries}))

    results = search(entries, query) if query else entries
    if region_filter != "All":
        results = [e for e in results if e.region == region_filter]
    if cuisine_filter != "All":
        results = [e for e in results if e.cuisine == cuisine_filter]

    st.write(f"Showing {len(results)} entries")
    for entry in results[:80]:
        with st.expander(entry.canonical_name):
            st.write(f"**Aliases:** {', '.join(entry.aliases)}")
            st.write(f"**Region:** {entry.region}")
            st.write(f"**Subregion:** {entry.subregion}")
            st.write(f"**Cuisine:** {entry.cuisine}")
            st.write(f"**Type:** {entry.food_type}")

with sources:
    st.subheader("Source hierarchy")
    st.markdown(
        """
1. Exact applicable regional food-composition source
2. IFCT / Pakistan food-composition reference
3. USDA for applicable generic or packaged foods
4. Ingredient-level recipe decomposition
5. Clearly labelled estimate
        """
    )
    st.markdown("### Attribution")
    st.write("Upstream architecture: zen-apps/ai-fitness-planner by Josh Janzen / zen-apps")
    st.write("Indian food composition: ICMR–NIN IFCT 2017")
    st.write("Pakistan food composition: FAO/INFOODS Pakistan resources")
    st.write("USDA: FoodData Central")
    st.caption("See NOTICE.md and docs/DATA_SOURCES.md for links and licensing notes.")
