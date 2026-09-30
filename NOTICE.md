# Notices and attribution

## Upstream project

This project was developed from the architecture and design patterns demonstrated by:

**AI Fitness Planner**  
https://github.com/zen-apps/ai-fitness-planner  
Copyright (c) 2025 Josh Janzen / zen-apps

The upstream repository is licensed under the MIT License. The upstream license text is preserved at:

`third_party_notices/ai-fitness-planner-LICENSE`

Upstream source inspected for this adaptation:

- commit: `2ff72d844d30c262eec6c945fc57f87223a994c5`
- branch: `main`

This project does not claim ownership of the upstream project or its original source code.

## Nutrition data sources

The project uses or is designed to use the following third-party/reference sources:

- USDA FoodData Central / USDA nutrition data — https://fdc.nal.usda.gov/
- Indian Food Composition Tables 2017 (ICMR–NIN) — https://www.nin.res.in/ebooks/IFCT2017.pdf
- FAO/INFOODS Pakistan food-composition resources — https://www.fao.org/infoods/infoods/tables-and-databases/pakistan/en/

The repository's South Asian ontology is a compatibility/normalization layer created for this project. It is not presented as an official government dataset and does not copy nutrient values from third-party tables.

Official third-party PDFs/data are intentionally not bundled by default. Users should obtain them from the authoritative source and follow the applicable terms of use.
