---
entity_id: "reaction.R01324"
entity_type: "reaction"
name: "citrate hydroxymutase"
source_database: "KEGG"
source_id: "R01324"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01324"
---

# citrate hydroxymutase

`reaction.R01324`

## Static

- Type: `reaction`
- Source: `KEGG:R01324`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Citrate Isocitrate

## Biological Role

Catalyzed by acnA (protein.P25516), acnB (protein.P36683). Substrates: Citrate (molecule.C00158). Products: Isocitrate (molecule.C00311).

## Annotation

Citrate <=> Isocitrate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P25516|protein.P25516]] `KEGG` `database` - via EC:4.2.1.3
- `catalyzes` <-- [[protein.P36683|protein.P36683]] `KEGG` `database` - via EC:4.2.1.3
- `is_product_of` <-- [[molecule.C00311|molecule.C00311]] `KEGG` `database` - C00158 <=> C00311
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `KEGG` `database` - C00158 <=> C00311

## External IDs

- `KEGG:R01324`

## Notes

EQUATION: C00158 <=> C00311
