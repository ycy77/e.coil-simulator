---
entity_id: "reaction.R00529"
entity_type: "reaction"
name: "ATP:sulfate adenylyltransferase"
source_database: "KEGG"
source_id: "R00529"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00529"
---

# ATP:sulfate adenylyltransferase

`reaction.R00529`

## Static

- Type: `reaction`
- Source: `KEGG:R00529`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Sulfate Diphosphate + Adenylyl sulfate

## Biological Role

Catalyzed by cysD (protein.P21156), cysN (protein.P23845). Substrates: ATP (molecule.C00002), Sulfate (molecule.C00059). Products: Diphosphate (molecule.C00013), Adenylyl sulfate (molecule.C00224).

## Annotation

ATP + Sulfate <=> Diphosphate + Adenylyl sulfate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21156|protein.P21156]] `KEGG` `database` - via EC:2.7.7.4
- `catalyzes` <-- [[protein.P23845|protein.P23845]] `KEGG` `database` - via EC:2.7.7.4
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00059 <=> C00013 + C00224
- `is_product_of` <-- [[molecule.C00224|molecule.C00224]] `KEGG` `database` - C00002 + C00059 <=> C00013 + C00224
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00059 <=> C00013 + C00224
- `is_substrate_of` <-- [[molecule.C00059|molecule.C00059]] `KEGG` `database` - C00002 + C00059 <=> C00013 + C00224

## External IDs

- `KEGG:R00529`

## Notes

EQUATION: C00002 + C00059 <=> C00013 + C00224
