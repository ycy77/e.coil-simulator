---
entity_id: "reaction.R12620"
entity_type: "reaction"
name: "(2E)-2-enoyl-CoA:NADP+ 4-oxidoreductase"
source_database: "KEGG"
source_id: "R12620"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12620"
---

# (2E)-2-enoyl-CoA:NADP+ 4-oxidoreductase

`reaction.R12620`

## Static

- Type: `reaction`
- Source: `KEGG:R12620`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

trans-2,3-Dehydroacyl-CoA + NADP+ (2E,4Z)-2,4-Dienoyl-CoA + NADPH + H+

## Biological Role

Catalyzed by fadH (protein.P42593). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

trans-2,3-Dehydroacyl-CoA + NADP+ <=> (2E,4Z)-2,4-Dienoyl-CoA + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P42593|protein.P42593]] `KEGG` `database` - via EC:1.3.1.34
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00658 + C00006 <=> C22258 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00658 + C00006 <=> C22258 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00658 + C00006 <=> C22258 + C00005 + C00080

## External IDs

- `KEGG:R12620`

## Notes

EQUATION: C00658 + C00006 <=> C22258 + C00005 + C00080
