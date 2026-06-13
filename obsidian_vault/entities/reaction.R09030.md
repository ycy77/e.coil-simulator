---
entity_id: "reaction.R09030"
entity_type: "reaction"
name: "D-allose-6-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R09030"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09030"
---

# D-allose-6-phosphate aldose-ketose-isomerase

`reaction.R09030`

## Static

- Type: `reaction`
- Source: `KEGG:R09030`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Allose 6-phosphate D-Allulose 6-phosphate

## Biological Role

Catalyzed by rpiA (protein.P0A7Z0), rpiB (protein.P37351). Substrates: D-Allose 6-phosphate (molecule.C02962). Products: D-Allulose 6-phosphate (molecule.C18096).

## Annotation

D-Allose 6-phosphate <=> D-Allulose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A7Z0|protein.P0A7Z0]] `KEGG` `database` - via EC:5.3.1.6
- `catalyzes` <-- [[protein.P37351|protein.P37351]] `KEGG` `database` - via EC:5.3.1.6
- `is_product_of` <-- [[molecule.C18096|molecule.C18096]] `KEGG` `database` - C02962 <=> C18096
- `is_substrate_of` <-- [[molecule.C02962|molecule.C02962]] `KEGG` `database` - C02962 <=> C18096

## External IDs

- `KEGG:R09030`

## Notes

EQUATION: C02962 <=> C18096
