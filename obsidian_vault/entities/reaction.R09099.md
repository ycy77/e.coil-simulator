---
entity_id: "reaction.R09099"
entity_type: "reaction"
name: "5,10-methylenetetrahydromethanopterin:glycine hydroxymethyltransferase"
source_database: "KEGG"
source_id: "R09099"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09099"
---

# 5,10-methylenetetrahydromethanopterin:glycine hydroxymethyltransferase

`reaction.R09099`

## Static

- Type: `reaction`
- Source: `KEGG:R09099`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Serine + 5,6,7,8-Tetrahydromethanopterin 5,10-Methylenetetrahydromethanopterin + Glycine + H2O

## Biological Role

Catalyzed by glyA (protein.P0A825). Substrates: L-Serine (molecule.C00065), 5,6,7,8-Tetrahydromethanopterin (molecule.C01217). Products: H2O (molecule.C00001), Glycine (molecule.C00037), 5,10-Methylenetetrahydromethanopterin (molecule.C04377).

## Annotation

L-Serine + 5,6,7,8-Tetrahydromethanopterin <=> 5,10-Methylenetetrahydromethanopterin + Glycine + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A825|protein.P0A825]] `KEGG` `database` - via EC:2.1.2.1
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00065 + C01217 <=> C04377 + C00037 + C00001
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C00065 + C01217 <=> C04377 + C00037 + C00001
- `is_product_of` <-- [[molecule.C04377|molecule.C04377]] `KEGG` `database` - C00065 + C01217 <=> C04377 + C00037 + C00001
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00065 + C01217 <=> C04377 + C00037 + C00001
- `is_substrate_of` <-- [[molecule.C01217|molecule.C01217]] `KEGG` `database` - C00065 + C01217 <=> C04377 + C00037 + C00001

## External IDs

- `KEGG:R09099`

## Notes

EQUATION: C00065 + C01217 <=> C04377 + C00037 + C00001
