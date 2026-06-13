---
entity_id: "molecule.C00855"
entity_type: "small_molecule"
name: "D-Methionine"
source_database: "KEGG"
source_id: "C00855"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Methionine"
  - "D-2-Amino-4-(methylthio)butyric acid"
---

# D-Methionine

`molecule.C00855`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00855`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Methionine; D-2-Amino-4-(methylthio)butyric acid

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: D-Methionine; D-2-Amino-4-(methylthio)butyric acid

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-202|reaction.ecocyc.TRANS-RXN0-202]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-202|reaction.ecocyc.TRANS-RXN0-202]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00855`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
