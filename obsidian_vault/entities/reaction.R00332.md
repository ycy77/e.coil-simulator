---
entity_id: "reaction.R00332"
entity_type: "reaction"
name: "ATP:GMP phosphotransferase"
source_database: "KEGG"
source_id: "R00332"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00332"
---

# ATP:GMP phosphotransferase

`reaction.R00332`

## Static

- Type: `reaction`
- Source: `KEGG:R00332`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + GMP ADP + GDP

## Biological Role

Catalyzed by gmk (protein.P60546). Substrates: ATP (molecule.C00002), GMP (molecule.C00144). Products: ADP (molecule.C00008), GDP (molecule.C00035).

## Annotation

ATP + GMP <=> ADP + GDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P60546|protein.P60546]] `KEGG` `database` - via EC:2.7.4.8
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00144 <=> C00008 + C00035
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00002 + C00144 <=> C00008 + C00035
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00144 <=> C00008 + C00035
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `KEGG` `database` - C00002 + C00144 <=> C00008 + C00035

## External IDs

- `KEGG:R00332`

## Notes

EQUATION: C00002 + C00144 <=> C00008 + C00035
