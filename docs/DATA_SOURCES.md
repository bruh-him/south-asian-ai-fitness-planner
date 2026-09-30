# Data sources and provenance

## 1. USDA FoodData Central

Primary site: https://fdc.nal.usda.gov/

The upstream `zen-apps/ai-fitness-planner` project distributes a sampled USDA branded-food JSON release. The local build process can download and compact that source for Claude Project use.

The compact file is deliberately not committed to this repository because it is large and reproducible.

## 2. Indian Food Composition Tables (IFCT 2017)

Publisher/reference: Indian Council of Medical Research — National Institute of Nutrition.

Official source: https://www.nin.res.in/ebooks/IFCT2017.pdf

Use this source for applicable Indian/South Indian raw foods and food-composition references when a relevant entry exists.

## 3. Pakistan food-composition resources

Reference portal: FAO/INFOODS Pakistan database page.

https://www.fao.org/infoods/infoods/tables-and-databases/pakistan/en/

Use the applicable Pakistan food-composition material for Pakistani ingredients/traditional foods when a relevant entry exists.

## 4. South Asian Food Ontology

`data/south_asian_food_ontology.csv`

This is an original project-created recognition layer. It exists to resolve:

- alternate spellings
- transliterations
- regional terminology
- canonical dish names
- cuisine/region
- food type
- typical ingredient families
- dietary classification

It deliberately contains **no fabricated nutrition values**.

## Food-source rule

```text
Exact applicable regional composition
        ↓
IFCT / Pakistan food-composition source
        ↓
USDA for applicable generic/packaged food
        ↓
ingredient-level recipe decomposition
        ↓
clearly labelled estimate
```
