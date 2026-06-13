---
entity_id: "reaction.R02622"
entity_type: "reaction"
name: "protein glutamine amidohydrolase"
source_database: "KEGG"
source_id: "R02622"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02622"
---

# protein glutamine amidohydrolase

`reaction.R02622`

## Static

- Type: `reaction`
- Source: `KEGG:R02622`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein glutamine + H2O Protein glutamate + Ammonia

## Biological Role

Catalyzed by cheB (protein.P07330). Substrates: H2O (molecule.C00001). Products: Ammonia (molecule.C00014).

## Annotation

Protein glutamine + H2O <=> Protein glutamate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07330|protein.P07330]] `KEGG` `database` - via EC:3.5.1.44
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C02583 + C00001 <=> C00614 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02583 + C00001 <=> C00614 + C00014

## External IDs

- `KEGG:R02622`

## Notes

EQUATION: C02583 + C00001 <=> C00614 + C00014
