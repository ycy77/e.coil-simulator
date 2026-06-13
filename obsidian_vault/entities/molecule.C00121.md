---
entity_id: "molecule.C00121"
entity_type: "small_molecule"
name: "D-Ribose"
source_database: "KEGG"
source_id: "C00121"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Ribose"
---

# D-Ribose

`molecule.C00121`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00121`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Ribose This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration. In decreasing order of frequency, the species of D-ribose in solution are CPD0-1110 (58.5%), CPD-15829 (21.5%), CPD0-1108 (13.5%), CPD-10330 (6.5%) and CPD-15818 "open chain" (0.05%) .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

KEGG compound: D-Ribose

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.MONOMER-60|complex.ecocyc.MONOMER-60]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R02137|reaction.R02137]] `KEGG` `database` - C00475 + C00001 <=> C00380 + C00121
- `is_substrate_of` --> [[reaction.ecocyc.R148-RXN|reaction.ecocyc.R148-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18819|reaction.ecocyc.RXN-18819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00121`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
