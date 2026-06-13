---
entity_id: "reaction.R00164"
entity_type: "reaction"
name: "phosphoprotein phosphohydrolase"
source_database: "KEGG"
source_id: "R00164"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00164"
---

# phosphoprotein phosphohydrolase

`reaction.R00164`

## Static

- Type: `reaction`
- Source: `KEGG:R00164`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphoprotein + H2O Protein + Orthophosphate

## Biological Role

Catalyzed by pphA (protein.P55798), pphB (protein.P55799). Substrates: H2O (molecule.C00001). Products: Orthophosphate (molecule.C00009), Protein (molecule.C00017).

## Annotation

Phosphoprotein + H2O <=> Protein + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P55798|protein.P55798]] `KEGG` `database` - via EC:3.1.3.16
- `catalyzes` <-- [[protein.P55799|protein.P55799]] `KEGG` `database` - via EC:3.1.3.16
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00562 + C00001 <=> C00017 + C00009
- `is_product_of` <-- [[molecule.C00017|molecule.C00017]] `KEGG` `database` - C00562 + C00001 <=> C00017 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00562 + C00001 <=> C00017 + C00009

## External IDs

- `KEGG:R00164`

## Notes

EQUATION: C00562 + C00001 <=> C00017 + C00009
