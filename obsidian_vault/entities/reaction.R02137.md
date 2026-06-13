---
entity_id: "reaction.R02137"
entity_type: "reaction"
name: "cytidine ribohydrolase"
source_database: "KEGG"
source_id: "R02137"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02137"
---

# cytidine ribohydrolase

`reaction.R02137`

## Static

- Type: `reaction`
- Source: `KEGG:R02137`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cytidine + H2O Cytosine + D-Ribose

## Biological Role

Catalyzed by rihB (protein.P33022). Substrates: H2O (molecule.C00001), Cytidine (molecule.C00475). Products: D-Ribose (molecule.C00121), Cytosine (molecule.C00380).

## Annotation

Cytidine + H2O <=> Cytosine + D-Ribose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33022|protein.P33022]] `KEGG` `database` - via EC:3.2.2.8
- `is_product_of` <-- [[molecule.C00121|molecule.C00121]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121
- `is_product_of` <-- [[molecule.C00380|molecule.C00380]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121

## External IDs

- `KEGG:R02137`

## Notes

EQUATION: C00475 + C00001 <=> C00380 + C00121
