---
entity_id: "molecule.C00181"
entity_type: "small_molecule"
name: "D-Xylose"
source_database: "KEGG"
source_id: "C00181"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Xylose"
  - "Wood sugar"
---

# D-Xylose

`molecule.C00181`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00181`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Xylose; Wood sugar This compound class represents a reducing sugar that exists in solution in multiple configurations. The open-chain structure shown here is provided only as a schematic illustration of chirality. Consult the appropriate class instances for information on specific ring structures and their anomeric configuration. At equlibrium D-Xylose is present in aqueous solution almost entirely in the pyranose form, with the following distribution: BETA-D-XYLOSE - 63%, CPD-25028 - 36.5%, CPD-25025 - >1%, CPD-25024 - >1%. The concentration of CPD-15377 is only 0.02% .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: D-Xylose; Wood sugar

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.ABC-33-RXN|reaction.ecocyc.ABC-33-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8773|reaction.ecocyc.RXN-8773]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-30|reaction.ecocyc.TRANS-RXN-30]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-33-RXN|reaction.ecocyc.ABC-33-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-30|reaction.ecocyc.TRANS-RXN-30]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-33-CPLX|complex.ecocyc.ABC-33-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AGF4|protein.P0AGF4]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00181`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
