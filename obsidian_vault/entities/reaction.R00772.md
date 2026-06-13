---
entity_id: "reaction.R00772"
entity_type: "reaction"
name: "D-mannose-6-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R00772"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00772"
---

# D-mannose-6-phosphate aldose-ketose-isomerase

`reaction.R00772`

## Static

- Type: `reaction`
- Source: `KEGG:R00772`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Mannose 6-phosphate D-Fructose 6-phosphate

## Biological Role

Catalyzed by manA (protein.P00946). Substrates: D-Mannose 6-phosphate (molecule.C00275). Products: D-Fructose 6-phosphate (molecule.C00085).

## Annotation

D-Mannose 6-phosphate <=> D-Fructose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P00946|protein.P00946]] `KEGG` `database` - via EC:5.3.1.8
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00275 <=> C00085
- `is_substrate_of` <-- [[molecule.C00275|molecule.C00275]] `KEGG` `database` - C00275 <=> C00085

## External IDs

- `KEGG:R00772`

## Notes

EQUATION: C00275 <=> C00085
