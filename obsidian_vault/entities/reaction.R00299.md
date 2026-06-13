---
entity_id: "reaction.R00299"
entity_type: "reaction"
name: "ATP:D-glucose 6-phosphotransferase"
source_database: "KEGG"
source_id: "R00299"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00299"
---

# ATP:D-glucose 6-phosphotransferase

`reaction.R00299`

## Static

- Type: `reaction`
- Source: `KEGG:R00299`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + D-Glucose ADP + D-Glucose 6-phosphate

## Biological Role

Catalyzed by glk (protein.P0A6V8). Substrates: ATP (molecule.C00002), D-Glucose (molecule.C00031). Products: ADP (molecule.C00008), D-Glucose 6-phosphate (molecule.C00092).

## Annotation

ATP + D-Glucose <=> ADP + D-Glucose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6V8|protein.P0A6V8]] `KEGG` `database` - via EC:2.7.1.2
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00031 <=> C00008 + C00092
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `KEGG` `database` - C00002 + C00031 <=> C00008 + C00092
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00031 <=> C00008 + C00092
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C00002 + C00031 <=> C00008 + C00092

## External IDs

- `KEGG:R00299`

## Notes

EQUATION: C00002 + C00031 <=> C00008 + C00092
