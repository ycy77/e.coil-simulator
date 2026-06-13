---
entity_id: "reaction.R04137"
entity_type: "reaction"
name: "3-hydroxyisovaleryl-CoA hydro-lyase"
source_database: "KEGG"
source_id: "R04137"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04137"
---

# 3-hydroxyisovaleryl-CoA hydro-lyase

`reaction.R04137`

## Static

- Type: `reaction`
- Source: `KEGG:R04137`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Hydroxyisovaleryl-CoA 3-Methylcrotonyl-CoA + H2O

## Biological Role

Catalyzed by fadB (protein.P21177), paaF (protein.P76082), fadJ (protein.P77399). Substrates: 3-Hydroxyisovaleryl-CoA (molecule.C05998). Products: H2O (molecule.C00001), 3-Methylcrotonyl-CoA (molecule.C03069).

## Annotation

3-Hydroxyisovaleryl-CoA <=> 3-Methylcrotonyl-CoA + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` <-- [[protein.P76082|protein.P76082]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `KEGG` `database` - via EC:4.2.1.17
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05998 <=> C03069 + C00001
- `is_product_of` <-- [[molecule.C03069|molecule.C03069]] `KEGG` `database` - C05998 <=> C03069 + C00001
- `is_substrate_of` <-- [[molecule.C05998|molecule.C05998]] `KEGG` `database` - C05998 <=> C03069 + C00001

## External IDs

- `KEGG:R04137`

## Notes

EQUATION: C05998 <=> C03069 + C00001
