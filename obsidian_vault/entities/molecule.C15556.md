---
entity_id: "molecule.C15556"
entity_type: "small_molecule"
name: "L-3,4-Dihydroxybutan-2-one 4-phosphate"
source_database: "KEGG"
source_id: "C15556"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-3,4-Dihydroxybutan-2-one 4-phosphate"
  - "1-Deoxy-L-glycero-tetrulose 4-phosphate"
  - "2-Hydroxy-3-oxobutyl phosphate"
---

# L-3,4-Dihydroxybutan-2-one 4-phosphate

`molecule.C15556`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15556`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-3,4-Dihydroxybutan-2-one 4-phosphate; 1-Deoxy-L-glycero-tetrulose 4-phosphate; 2-Hydroxy-3-oxobutyl phosphate EcoCyc common name: 1-deoxy-L-glycero-tetrulose 4-phosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: L-3,4-Dihydroxybutan-2-one 4-phosphate; 1-Deoxy-L-glycero-tetrulose 4-phosphate; 2-Hydroxy-3-oxobutyl phosphate

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R07281|reaction.R07281]] `KEGG` `database` - C00199 <=> C15556 + C00058
- `is_product_of` --> [[reaction.ecocyc.DIOHBUTANONEPSYN-RXN|reaction.ecocyc.DIOHBUTANONEPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.LUMAZINESYN-RXN|reaction.ecocyc.LUMAZINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C15556`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
