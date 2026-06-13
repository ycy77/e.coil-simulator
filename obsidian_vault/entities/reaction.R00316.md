---
entity_id: "reaction.R00316"
entity_type: "reaction"
name: "ATP:acetate adenylyltransferase"
source_database: "KEGG"
source_id: "R00316"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00316"
---

# ATP:acetate adenylyltransferase

`reaction.R00316`

## Static

- Type: `reaction`
- Source: `KEGG:R00316`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Acetate Diphosphate + Acetyl adenylate

## Biological Role

Catalyzed by acs (protein.P27550). Substrates: ATP (molecule.C00002), Acetate (molecule.C00033). Products: Diphosphate (molecule.C00013), Acetyl adenylate (molecule.C05993).

## Annotation

ATP + Acetate <=> Diphosphate + Acetyl adenylate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27550|protein.P27550]] `KEGG` `database` - via EC:6.2.1.1
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00033 <=> C00013 + C05993
- `is_product_of` <-- [[molecule.C05993|molecule.C05993]] `KEGG` `database` - C00002 + C00033 <=> C00013 + C05993
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00033 <=> C00013 + C05993
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00002 + C00033 <=> C00013 + C05993

## External IDs

- `KEGG:R00316`

## Notes

EQUATION: C00002 + C00033 <=> C00013 + C05993
