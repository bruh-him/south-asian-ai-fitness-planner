# South Asian AI Fitness Planner

A professionally structured South Asian adaptation of the architecture demonstrated by `zen-apps/ai-fitness-planner`.

This project translates the reference fitness-planning architecture into a Pakistan-aware, India-aware, and South-India-aware nutrition and hypertrophy planning system designed especially for Claude Projects.

> **Important:** This repository does not pretend that the original Python/LangGraph/FAISS/MongoDB backend is running inside Claude Projects. It translates the useful architecture into a rigorous, auditable Claude Project workflow and adds a culturally aware nutrition data layer.

## What this project adds

| Capability | Reference | This project |
|---|---|---|
| Multi-agent planning | Yes | Translated + strengthened |
| Profile validation | Yes | Expanded health/training intake |
| BMR/TDEE | Yes | Scientific override layer |
| Fixed macro split | Legacy | Replaced with constraint-based macros |
| USDA foods | Yes | Compact source pipeline |
| Pakistani foods | Limited | First-class food ontology |
| Indian foods | Limited | IFCT-aware source strategy |
| South Indian foods | Limited | Dedicated recognition + cuisine layer |
| Recipe decomposition | Limited | Explicit ingredient-composition workflow |
| Food-source attribution | Partial | Required |
| QA pass | Limited | Independent planning audit |
| Adaptive coaching | Not core | Versioned feedback loop |
| Claude Project prompts | No | Included |
| GUI companion | No | Included |

## Architecture

```text
USER PROFILE
    |
PROFILE MANAGER
    |
ENERGY & NUTRITION ENGINE
    |
FOOD SOURCE RESOLVER
    |
MEAL PLANNER ------ WORKOUT ARCHITECT
    |                    |
    +---- COORDINATION -+
               |
        QUALITY ASSURANCE
               |
        FINAL SYNTHESIS
               |
        ADAPTIVE REVISION
```

## South Asian food coverage

The recognition layer is designed for Pakistani, Indian, and South Indian foods including biryani, karahi, nihari, haleem, dal, chole, rajma, roti, paratha, idli, dosa, sambar, rasam, pongal, upma, puttu, appam, chicken Chettinad, Hyderabadi biryani, palak paneer, mango, guava, pomegranate, and dates.

The ontology is a recognition and normalization layer, not a nutrient database. Missing dishes can be handled through transparent ingredient-level recipe decomposition using an applicable composition source.

## Data-source policy

The project separates food recognition from food composition.

- The South Asian ontology is project-authored and does not fabricate nutrient values.
- USDA data is downloaded and compacted locally rather than committing a large generated dataset.
- Indian composition references use the Indian Food Composition Tables (ICMR-NIN).
- Pakistani composition references use applicable FAO/INFOODS Pakistan resources.
- Official third-party PDFs are not redistributed by default.

See `docs/DATA_SOURCES.md` and `NOTICE.md`.

## Claude Project integration

The `claude/` directory contains the Project Operating System, architecture bootstrap, intake, full-plan, adaptive-coaching, and state-snapshot prompts.

Start with:

1. `claude/project_instructions.md`
2. `claude/bootstrap_prompt.md`
3. `claude/intake_prompt.md`
4. `claude/full_plan_prompt.md`
5. `claude/adaptive_coaching_prompt.md`
6. `claude/state_snapshot_prompt.md`

## GUI companion

A lightweight Streamlit companion is included for presentation and food-ontology exploration.

```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Upstream credit

The architecture and substantial implementation ideas are based on **AI Fitness Planner** by **Josh Janzen / zen-apps**:

https://github.com/zen-apps/ai-fitness-planner

The upstream project is MIT licensed. Its license and attribution are preserved in `third_party_notices/`.

## Health and safety

This project is software and planning infrastructure, not a medical diagnosis system. Nutrition estimates vary with recipes, cooking methods, body composition, activity, and individual health conditions. Clinically significant symptoms require appropriate professional assessment.

## License

Project code is released under the MIT License. Third-party material remains subject to its original licenses and terms. See `NOTICE.md`.
