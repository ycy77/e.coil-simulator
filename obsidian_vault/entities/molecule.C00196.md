---
entity_id: "molecule.C00196"
entity_type: "small_molecule"
name: "2,3-Dihydroxybenzoate"
source_database: "KEGG"
source_id: "C00196"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2,3-Dihydroxybenzoate"
  - "2,3-Dihydroxybenzoic acid"
---

# 2,3-Dihydroxybenzoate

`molecule.C00196`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00196`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2,3-Dihydroxybenzoate; 2,3-Dihydroxybenzoic acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

KEGG compound: 2,3-Dihydroxybenzoate; 2,3-Dihydroxybenzoic acid

## Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.DHBDEHYD-RXN|reaction.ecocyc.DHBDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7105|reaction.ecocyc.RXN0-7105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DHBAMPLIG-RXN|reaction.ecocyc.DHBAMPLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ENTMULTI-RXN|reaction.ecocyc.ENTMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19445|reaction.ecocyc.RXN-19445]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2943|reaction.ecocyc.RXN0-2943]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00196`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
