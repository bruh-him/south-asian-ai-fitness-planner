# Architecture

## Upstream architecture

The reference repository implements a real LangGraph-based workflow with coordinated profile, meal, workout, coordination and summary stages.

The adaptation retains the useful conceptual architecture but is optimized for Claude Projects rather than claiming that Claude is literally running the original Python backend.

## Adapted state machine

```text
PROFILE_MANAGER
      ↓
NUTRITION_ENGINE
      ↓
FOOD_SOURCE_RESOLVER
      ↓
MEAL_PLANNER ─────────┐
                      ↓
WORKOUT_ARCHITECT → COORDINATION_ENGINE
                              ↓
                       QUALITY_ASSURANCE
                              ↓
                       FINAL_SYNTHESIS
                              ↓
                       PROGRESS_TRACKER
                              ↓
                       ADAPTIVE_REVISION
```

## State

- `PROFILE_STATE`
- `NUTRITION_STATE`
- `TRAINING_STATE`
- `CONSTRAINT_STATE`
- `RECOVERY_STATE`
- `FOOD_SOURCE_STATE`
- `EVIDENCE_STATE`
- `QA_STATE`

## Critical distinction

Python/LangGraph/FAISS/MongoDB source files are architecture references unless an actual runtime is used.

The Claude workflow should never claim an external computation or database lookup that did not occur.
