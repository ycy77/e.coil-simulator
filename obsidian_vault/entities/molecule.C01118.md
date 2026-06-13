---
entity_id: "molecule.C01118"
entity_type: "small_molecule"
name: "O-Succinyl-L-homoserine"
source_database: "KEGG"
source_id: "C01118"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "O-Succinyl-L-homoserine"
  - "O4-Succinyl-L-homoserine"
  - "O-Succinylhomoserine"
---

# O-Succinyl-L-homoserine

`molecule.C01118`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01118`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: O-Succinyl-L-homoserine; O4-Succinyl-L-homoserine; O-Succinylhomoserine

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: O-Succinyl-L-homoserine; O4-Succinyl-L-homoserine; O-Succinylhomoserine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.HOMSUCTRAN-RXN|reaction.ecocyc.HOMSUCTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00999|reaction.R00999]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.METBALT-RXN|reaction.ecocyc.METBALT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN|reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15147|reaction.ecocyc.RXN-15147]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01118`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
