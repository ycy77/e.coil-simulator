---
entity_id: "reaction.R00345"
entity_type: "reaction"
name: "phosphate:oxaloacetate carboxy-lyase (adding phosphate;phosphoenolpyruvate-forming)"
source_database: "KEGG"
source_id: "R00345"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00345"
---

# phosphate:oxaloacetate carboxy-lyase (adding phosphate;phosphoenolpyruvate-forming)

`reaction.R00345`

## Static

- Type: `reaction`
- Source: `KEGG:R00345`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Orthophosphate + Oxaloacetate H2O + Phosphoenolpyruvate + CO2

## Biological Role

Catalyzed by ppc (protein.P00864). Substrates: Orthophosphate (molecule.C00009), Oxaloacetate (molecule.C00036). Products: H2O (molecule.C00001), CO2 (molecule.C00011), Phosphoenolpyruvate (molecule.C00074).

## Annotation

Orthophosphate + Oxaloacetate <=> H2O + Phosphoenolpyruvate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00864|protein.P00864]] `KEGG` `database` - via EC:4.1.1.31
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00009 + C00036 <=> C00001 + C00074 + C00011

## External IDs

- `KEGG:R00345`

## Notes

EQUATION: C00009 + C00036 <=> C00001 + C00074 + C00011
