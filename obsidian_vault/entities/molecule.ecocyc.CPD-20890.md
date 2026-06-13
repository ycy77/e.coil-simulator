---
entity_id: "molecule.ecocyc.CPD-20890"
entity_type: "small_molecule"
name: "tetraphenylphosphonium"
source_database: "EcoCyc"
source_id: "CPD-20890"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "TPP+"
---

# tetraphenylphosphonium

`molecule.ecocyc.CPD-20890`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CPD-20890`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound CPD-20890

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Annotation

EcoCyc compound CPD-20890

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-348|reaction.ecocyc.TRANS-RXN-348]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-635|reaction.ecocyc.TRANS-RXN0-635]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-348|reaction.ecocyc.TRANS-RXN-348]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-635|reaction.ecocyc.TRANS-RXN0-635]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN-369|reaction.ecocyc.TRANS-RXN-369]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:CPD-20890`
- `LIGAND-CPD:C11152`
- `PUBCHEM:164912`
- `CHEBI:44880`

## Notes

(C 24)
