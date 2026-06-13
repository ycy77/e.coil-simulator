---
entity_id: "reaction.R00510"
entity_type: "reaction"
name: "cytidine-5'-monophosphate phosphoribohydrolase"
source_database: "KEGG"
source_id: "R00510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00510"
---

# cytidine-5'-monophosphate phosphoribohydrolase

`reaction.R00510`

## Static

- Type: `reaction`
- Source: `KEGG:R00510`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CMP + H2O Cytosine + D-Ribose 5-phosphate

## Biological Role

Catalyzed by ppnN (protein.P0ADR8). Substrates: H2O (molecule.C00001), CMP (molecule.C00055). Products: D-Ribose 5-phosphate (molecule.C00117), Cytosine (molecule.C00380).

## Annotation

CMP + H2O <=> Cytosine + D-Ribose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ADR8|protein.P0ADR8]] `KEGG` `database` - via EC:3.2.2.10
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117
- `is_product_of` <-- [[molecule.C00380|molecule.C00380]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117
- `is_substrate_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117

## External IDs

- `KEGG:R00510`

## Notes

EQUATION: C00055 + C00001 <=> C00380 + C00117
