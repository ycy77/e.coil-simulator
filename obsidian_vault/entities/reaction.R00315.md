---
entity_id: "reaction.R00315"
entity_type: "reaction"
name: "ATP:acetate phosphotransferase"
source_database: "KEGG"
source_id: "R00315"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00315"
---

# ATP:acetate phosphotransferase

`reaction.R00315`

## Static

- Type: `reaction`
- Source: `KEGG:R00315`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Acetate ADP + Acetyl phosphate

## Biological Role

Catalyzed by ackA (protein.P0A6A3), tdcD (protein.P11868). Substrates: ATP (molecule.C00002), Acetate (molecule.C00033). Products: ADP (molecule.C00008), Acetyl phosphate (molecule.C00227).

## Annotation

ATP + Acetate <=> ADP + Acetyl phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6A3|protein.P0A6A3]] `KEGG` `database` - via EC:2.7.2.1
- `catalyzes` <-- [[protein.P11868|protein.P11868]] `KEGG` `database` - via EC:2.7.2.15
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00033 <=> C00008 + C00227
- `is_product_of` <-- [[molecule.C00227|molecule.C00227]] `KEGG` `database` - C00002 + C00033 <=> C00008 + C00227
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00033 <=> C00008 + C00227
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00002 + C00033 <=> C00008 + C00227

## External IDs

- `KEGG:R00315`

## Notes

EQUATION: C00002 + C00033 <=> C00008 + C00227
