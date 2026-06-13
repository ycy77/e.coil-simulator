---
entity_id: "reaction.R00199"
entity_type: "reaction"
name: "ATP:pyruvate,water phosphotransferase"
source_database: "KEGG"
source_id: "R00199"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00199"
---

# ATP:pyruvate,water phosphotransferase

`reaction.R00199`

## Static

- Type: `reaction`
- Source: `KEGG:R00199`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Pyruvate + H2O AMP + Phosphoenolpyruvate + Orthophosphate

## Biological Role

Catalyzed by ppsA (protein.P23538). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Pyruvate (molecule.C00022). Products: Orthophosphate (molecule.C00009), AMP (molecule.C00020), Phosphoenolpyruvate (molecule.C00074).

## Annotation

ATP + Pyruvate + H2O <=> AMP + Phosphoenolpyruvate + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23538|protein.P23538]] `KEGG` `database` - via EC:2.7.9.2
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009

## External IDs

- `KEGG:R00199`

## Notes

EQUATION: C00002 + C00022 + C00001 <=> C00020 + C00074 + C00009
