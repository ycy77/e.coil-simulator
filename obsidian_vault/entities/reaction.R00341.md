---
entity_id: "reaction.R00341"
entity_type: "reaction"
name: "ATP:oxaloacetate carboxy-lyase (transphosphorylating;phosphoenolpyruvate-forming)"
source_database: "KEGG"
source_id: "R00341"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00341"
---

# ATP:oxaloacetate carboxy-lyase (transphosphorylating;phosphoenolpyruvate-forming)

`reaction.R00341`

## Static

- Type: `reaction`
- Source: `KEGG:R00341`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Oxaloacetate ADP + Phosphoenolpyruvate + CO2

## Biological Role

Catalyzed by pckA (protein.P22259). Substrates: ATP (molecule.C00002), Oxaloacetate (molecule.C00036). Products: ADP (molecule.C00008), CO2 (molecule.C00011), Phosphoenolpyruvate (molecule.C00074).

## Annotation

ATP + Oxaloacetate <=> ADP + Phosphoenolpyruvate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P22259|protein.P22259]] `KEGG` `database` - via EC:4.1.1.49
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00002 + C00036 <=> C00008 + C00074 + C00011

## External IDs

- `KEGG:R00341`

## Notes

EQUATION: C00002 + C00036 <=> C00008 + C00074 + C00011
