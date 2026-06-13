---
entity_id: "reaction.R03774"
entity_type: "reaction"
name: "L-rhamnonate hydro-lyase"
source_database: "KEGG"
source_id: "R03774"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03774"
---

# L-rhamnonate hydro-lyase

`reaction.R03774`

## Static

- Type: `reaction`
- Source: `KEGG:R03774`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Rhamnonate 2-Dehydro-3-deoxy-L-rhamnonate + H2O

## Biological Role

Catalyzed by rhmD (protein.P77215). Substrates: L-Rhamnonate (molecule.C01934). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-L-rhamnonate (molecule.C03979).

## Annotation

L-Rhamnonate <=> 2-Dehydro-3-deoxy-L-rhamnonate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77215|protein.P77215]] `KEGG` `database` - via EC:4.2.1.90
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01934 <=> C03979 + C00001
- `is_product_of` <-- [[molecule.C03979|molecule.C03979]] `KEGG` `database` - C01934 <=> C03979 + C00001
- `is_substrate_of` <-- [[molecule.C01934|molecule.C01934]] `KEGG` `database` - C01934 <=> C03979 + C00001

## External IDs

- `KEGG:R03774`

## Notes

EQUATION: C01934 <=> C03979 + C00001
