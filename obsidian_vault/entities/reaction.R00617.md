---
entity_id: "reaction.R00617"
entity_type: "reaction"
name: "ATP:thiamin-phosphate phosphotransferase"
source_database: "KEGG"
source_id: "R00617"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00617"
---

# ATP:thiamin-phosphate phosphotransferase

`reaction.R00617`

## Static

- Type: `reaction`
- Source: `KEGG:R00617`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Thiamin monophosphate ADP + Thiamin diphosphate

## Biological Role

Catalyzed by thiL (protein.P0AGG0). Substrates: ATP (molecule.C00002), Thiamin monophosphate (molecule.C01081). Products: ADP (molecule.C00008), Thiamin diphosphate (molecule.C00068).

## Annotation

ATP + Thiamin monophosphate <=> ADP + Thiamin diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGG0|protein.P0AGG0]] `KEGG` `database` - via EC:2.7.4.16
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C01081 <=> C00008 + C00068
- `is_product_of` <-- [[molecule.C00068|molecule.C00068]] `KEGG` `database` - C00002 + C01081 <=> C00008 + C00068
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C01081 <=> C00008 + C00068
- `is_substrate_of` <-- [[molecule.C01081|molecule.C01081]] `KEGG` `database` - C00002 + C01081 <=> C00008 + C00068

## External IDs

- `KEGG:R00617`

## Notes

EQUATION: C00002 + C01081 <=> C00008 + C00068
