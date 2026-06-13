---
entity_id: "reaction.R00769"
entity_type: "reaction"
name: "UTP:D-fructose-6-phosphate 1-phosphotransferase"
source_database: "KEGG"
source_id: "R00769"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00769"
---

# UTP:D-fructose-6-phosphate 1-phosphotransferase

`reaction.R00769`

## Static

- Type: `reaction`
- Source: `KEGG:R00769`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + D-Fructose 6-phosphate UDP + D-Fructose 1,6-bisphosphate

## Biological Role

Catalyzed by pfkB (protein.P06999), pfkA (protein.P0A796). Substrates: UTP (molecule.C00075), D-Fructose 6-phosphate (molecule.C00085). Products: UDP (molecule.C00015), D-Fructose 1,6-bisphosphate (molecule.C00354).

## Annotation

UTP + D-Fructose 6-phosphate <=> UDP + D-Fructose 1,6-bisphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06999|protein.P06999]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` <-- [[protein.P0A796|protein.P0A796]] `KEGG` `database` - via EC:2.7.1.11
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354
- `is_product_of` <-- [[molecule.C00354|molecule.C00354]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354
- `is_substrate_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00075 + C00085 <=> C00015 + C00354

## External IDs

- `KEGG:R00769`

## Notes

EQUATION: C00075 + C00085 <=> C00015 + C00354
