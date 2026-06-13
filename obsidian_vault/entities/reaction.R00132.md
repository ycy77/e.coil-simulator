---
entity_id: "reaction.R00132"
entity_type: "reaction"
name: "carbonate hydro-lyase (carbon-dioxide-forming);"
source_database: "KEGG"
source_id: "R00132"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00132"
---

# carbonate hydro-lyase (carbon-dioxide-forming);

`reaction.R00132`

## Static

- Type: `reaction`
- Source: `KEGG:R00132`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Carbonic acid CO2 + H2O

## Biological Role

Catalyzed by cynT (protein.P0ABE9), can (protein.P61517). Products: H2O (molecule.C00001), CO2 (molecule.C00011).

## Annotation

Carbonic acid <=> CO2 + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0ABE9|protein.P0ABE9]] `KEGG` `database` - via EC:4.2.1.1
- `catalyzes` <-- [[protein.P61517|protein.P61517]] `KEGG` `database` - via EC:4.2.1.1
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01353 <=> C00011 + C00001
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C01353 <=> C00011 + C00001

## External IDs

- `KEGG:R00132`

## Notes

EQUATION: C01353 <=> C00011 + C00001
