---
entity_id: "molecule.C01487"
entity_type: "small_molecule"
name: "D-Allose"
source_database: "KEGG"
source_id: "C01487"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Allose"
---

# D-Allose

`molecule.C01487`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01487`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Allose Each aldopentose or aldohexose exists as a mixture of at least six compounds: the aldehyde, the hydrated aldehyde (gem-diol), the two pyranoses, and the two furanoses. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration. The relative ratios of the different allose tautomers was reported to be as follows (in : Pyranose form: CPD-15627/CPD-15628 15%/85% Furanose form: CPD-16933/CPD-16934 41%/59%

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: D-Allose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2482|complex.ecocyc.MONOMER0-2482]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ABC-42-RXN|reaction.ecocyc.ABC-42-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-42-RXN|reaction.ecocyc.ABC-42-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4942|reaction.ecocyc.RXN0-4942]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-42-CPLX|complex.ecocyc.ABC-42-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01487`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
