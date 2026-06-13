---
entity_id: "reaction.R00660"
entity_type: "reaction"
name: "phosphoenolpyruvate:UDP-N-acetyl-D-glucosamine 1-carboxyvinyl-transferase"
source_database: "KEGG"
source_id: "R00660"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00660"
---

# phosphoenolpyruvate:UDP-N-acetyl-D-glucosamine 1-carboxyvinyl-transferase

`reaction.R00660`

## Static

- Type: `reaction`
- Source: `KEGG:R00660`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphoenolpyruvate + UDP-N-acetyl-alpha-D-glucosamine UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine + Orthophosphate

## Biological Role

Catalyzed by murA (protein.P0A749). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), Phosphoenolpyruvate (molecule.C00074). Products: Orthophosphate (molecule.C00009), UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine (molecule.C04631).

## Annotation

Phosphoenolpyruvate + UDP-N-acetyl-alpha-D-glucosamine <=> UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A749|protein.P0A749]] `KEGG` `database` - via EC:2.5.1.7
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009
- `is_product_of` <-- [[molecule.C04631|molecule.C04631]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009

## External IDs

- `KEGG:R00660`

## Notes

EQUATION: C00074 + C00043 <=> C04631 + C00009
