---
entity_id: "reaction.R13011"
entity_type: "reaction"
name: "2-oxoadipate dioxygenase/carboxy lyase"
source_database: "KEGG"
source_id: "R13011"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13011"
---

# 2-oxoadipate dioxygenase/carboxy lyase

`reaction.R13011`

## Static

- Type: `reaction`
- Source: `KEGG:R13011`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxoadipate + Oxygen (R)-2-Hydroxyglutarate + CO2

## Biological Role

Catalyzed by ydcJ (protein.P76097). Substrates: Oxygen (molecule.C00007), 2-Oxoadipate (molecule.C00322). Products: CO2 (molecule.C00011), (R)-2-Hydroxyglutarate (molecule.C01087).

## Annotation

2-Oxoadipate + Oxygen <=> (R)-2-Hydroxyglutarate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76097|protein.P76097]] `KEGG` `database` - via EC:1.13.11.93
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00322 + C00007 <=> C01087 + C00011
- `is_product_of` <-- [[molecule.C01087|molecule.C01087]] `KEGG` `database` - C00322 + C00007 <=> C01087 + C00011
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00322 + C00007 <=> C01087 + C00011
- `is_substrate_of` <-- [[molecule.C00322|molecule.C00322]] `KEGG` `database` - C00322 + C00007 <=> C01087 + C00011

## External IDs

- `KEGG:R13011`

## Notes

EQUATION: C00322 + C00007 <=> C01087 + C00011
