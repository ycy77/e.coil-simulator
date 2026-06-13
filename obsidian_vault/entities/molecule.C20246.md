---
entity_id: "molecule.C20246"
entity_type: "small_molecule"
name: "2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate"
source_database: "KEGG"
source_id: "C20246"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate"
  - "cThz*-P"
---

# 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate

`molecule.C20246`

## Static

- Type: `small_molecule`
- Source: `KEGG:C20246`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate; cThz*-P

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Annotation

KEGG compound: 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate; cThz*-P

## Pathways

- `eco00730` Thiamine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R10247|reaction.R10247]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_product_of` --> [[reaction.ecocyc.RXN0-7196|reaction.ecocyc.RXN0-7196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THIAZOLSYN2-RXN|reaction.ecocyc.THIAZOLSYN2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12611|reaction.ecocyc.RXN-12611]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C20246`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
