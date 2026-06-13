---
entity_id: "molecule.C00979"
entity_type: "small_molecule"
name: "O-Acetyl-L-serine"
source_database: "KEGG"
source_id: "C00979"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "O-Acetyl-L-serine"
  - "O3-Acetyl-L-serine"
---

# O-Acetyl-L-serine

`molecule.C00979`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00979`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: O-Acetyl-L-serine; O3-Acetyl-L-serine

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: O-Acetyl-L-serine; O3-Acetyl-L-serine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2781|complex.ecocyc.CPLX0-2781]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00586|reaction.R00586]] `KEGG` `database` - C00065 + C00024 <=> C00979 + C00010
- `is_product_of` --> [[reaction.ecocyc.RXN0-1923|reaction.ecocyc.RXN0-1923]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SERINE-O-ACETTRAN-RXN|reaction.ecocyc.SERINE-O-ACETTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03132|reaction.R03132]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_substrate_of` --> [[reaction.ecocyc.ACSERLY-RXN|reaction.ecocyc.ACSERLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1923|reaction.ecocyc.RXN0-1923]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3001|reaction.ecocyc.RXN0-3001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SULFOCYS-RXN|reaction.ecocyc.SULFOCYS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00979`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
