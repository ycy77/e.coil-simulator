---
entity_id: "reaction.R12589"
entity_type: "reaction"
name: "xanthosine 5'-triphosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R12589"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12589"
---

# xanthosine 5'-triphosphate phosphohydrolase

`reaction.R12589`

## Static

- Type: `reaction`
- Source: `KEGG:R12589`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

XTP + H2O XDP + Orthophosphate

## Biological Role

Catalyzed by yjjX (protein.P39411). Substrates: H2O (molecule.C00001), XTP (molecule.C00700). Products: Orthophosphate (molecule.C00009).

## Annotation

XTP + H2O <=> XDP + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P39411|protein.P39411]] `KEGG` `database` - via EC:3.6.1.73
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00700 + C00001 <=> C01337 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00700 + C00001 <=> C01337 + C00009
- `is_substrate_of` <-- [[molecule.C00700|molecule.C00700]] `KEGG` `database` - C00700 + C00001 <=> C01337 + C00009

## External IDs

- `KEGG:R12589`

## Notes

EQUATION: C00700 + C00001 <=> C01337 + C00009
