# Claude Project deployment guide

## Knowledge

Upload:

- `claude/project_instructions.md`
- `claude/bootstrap_prompt.md`
- `claude/intake_prompt.md`
- `claude/full_plan_prompt.md`
- `claude/adaptive_coaching_prompt.md`
- `claude/state_snapshot_prompt.md`
- `data/south_asian_food_ontology.csv`
- the compact USDA CSV generated locally
- the official IFCT/Pakistan composition documents obtained from their authoritative sources
- the upstream architecture files selected for reference

## Recommended model profile

Use the strongest Sonnet-class model available on the user's Claude plan. Use high effort for normal complete-plan generation. Reserve the maximum effort setting for difficult architecture/evidence audits because higher effort consumes more usage.

## Operating pattern

1. Bootstrap/audit the knowledge base.
2. Run intake.
3. Freeze a validated profile.
4. Run the complete multi-agent plan.
5. Activate adaptive coaching.
6. Save a state snapshot after meaningful revisions.

Do not repeatedly attach the same knowledge files to every chat. Keep stable material in Project Knowledge.
