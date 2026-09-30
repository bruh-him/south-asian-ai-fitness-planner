Do not generate a fitness plan yet.

Audit the project knowledge and reconstruct the architecture represented by the upstream source.

1. Identify actual agent classes and workflow nodes.
2. Reconstruct the LangGraph execution path.
3. Map profile, workflow-state, meal, workout and summary schemas.
4. Extract actual BMR/TDEE/macro logic and identify legacy assumptions.
5. Identify which parts can be simulated in Claude Projects and which require a runtime.
6. Audit the USDA compact dataset, South Asian ontology, Indian IFCT reference and Pakistan food-composition reference.
7. Treat the ontology as recognition/normalization, not as a nutrient database.
8. Build a regional food-source decision tree.
9. Test recognition on Chicken Biryani, Chicken Karahi, Nihari, Haleem, Daal Chana, Chapati, Paratha, Idli, Dosa, Masala Dosa, Sambar, Rasam, Pongal, Upma, Puttu, Chicken Chettinad, Hyderabadi Biryani, Palak Paneer, Rajma, Chole, Mango, Guava, Pomegranate and Dates.
10. Produce a SOURCE-OF-TRUTH MAP, LEGACY-LOGIC RISKS, CLAUDE TRANSLATION, FINAL STATE MACHINE, DATA REQUIREMENTS, QA REQUIREMENTS and SOUTH ASIAN FOOD-SOURCE ARCHITECTURE.

Do not claim that Python, LangGraph, FAISS or MongoDB executed.
