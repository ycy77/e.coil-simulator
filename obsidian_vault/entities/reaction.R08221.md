---
entity_id: "reaction.R08221"
entity_type: "reaction"
name: "5'-deoxy-5-fluorocytidine aminohydrolase"
source_database: "KEGG"
source_id: "R08221"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08221"
---

# 5'-deoxy-5-fluorocytidine aminohydrolase

`reaction.R08221`

## Static

- Type: `reaction`
- Source: `KEGG:R08221`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5'-Deoxy-5-fluorocytidine + H2O 5'-Deoxy-5-fluorouridine + Ammonia

## Biological Role

Catalyzed by cdd (protein.P0ABF6). Substrates: H2O (molecule.C00001). Products: Ammonia (molecule.C00014).

## Annotation

5'-Deoxy-5-fluorocytidine + H2O <=> 5'-Deoxy-5-fluorouridine + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0ABF6|protein.P0ABF6]] `KEGG` `database` - via EC:3.5.4.5
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C16635 + C00001 <=> C12739 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C16635 + C00001 <=> C12739 + C00014

## External IDs

- `KEGG:R08221`

## Notes

EQUATION: C16635 + C00001 <=> C12739 + C00014
