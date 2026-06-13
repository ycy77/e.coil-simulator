---
entity_id: "reaction.R12621"
entity_type: "reaction"
name: "5'-deoxyadenosine ribohydrolase"
source_database: "KEGG"
source_id: "R12621"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12621"
---

# 5'-deoxyadenosine ribohydrolase

`reaction.R12621`

## Static

- Type: `reaction`
- Source: `KEGG:R12621`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5'-Deoxyadenosine + H2O 5-Deoxy-D-ribose + Adenine

## Biological Role

Catalyzed by mtnN (protein.P0AF12). Substrates: H2O (molecule.C00001). Products: Adenine (molecule.C00147).

## Annotation

5'-Deoxyadenosine + H2O <=> 5-Deoxy-D-ribose + Adenine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AF12|protein.P0AF12]] `KEGG` `database` - via EC:3.2.2.9
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `KEGG` `database` - C05198 + C00001 <=> C22288 + C00147
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05198 + C00001 <=> C22288 + C00147

## External IDs

- `KEGG:R12621`

## Notes

EQUATION: C05198 + C00001 <=> C22288 + C00147
