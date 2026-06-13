---
entity_id: "reaction.R08880"
entity_type: "reaction"
name: "L-idonate:NADP+ 2-oxidoreductase"
source_database: "KEGG"
source_id: "R08880"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08880"
---

# L-idonate:NADP+ 2-oxidoreductase

`reaction.R08880`

## Static

- Type: `reaction`
- Source: `KEGG:R08880`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Idonate + NADP+ 2-Dehydro-L-idonate + NADPH + H+

## Biological Role

Catalyzed by ghrB (protein.P37666). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

L-Idonate + NADP+ <=> 2-Dehydro-L-idonate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P37666|protein.P37666]] `KEGG` `database` - via EC:1.1.1.215
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00770 + C00006 <=> C15673 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00770 + C00006 <=> C15673 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00770 + C00006 <=> C15673 + C00005 + C00080

## External IDs

- `KEGG:R08880`

## Notes

EQUATION: C00770 + C00006 <=> C15673 + C00005 + C00080
