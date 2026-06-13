---
entity_id: "molecule.ecocyc.CPD-15979"
entity_type: "small_molecule"
name: "D-mannopyranose 6-phosphate"
source_database: "EcoCyc"
source_id: "CPD-15979"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "D-mannopyranose-6-P"
---

# D-mannopyranose 6-phosphate

`molecule.ecocyc.CPD-15979`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CPD-15979`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound CPD-15979

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Annotation

EcoCyc compound CPD-15979

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.MANNKIN-RXN|reaction.ecocyc.MANNKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSMANMUT-RXN|reaction.ecocyc.PHOSMANMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5216|reaction.ecocyc.RXN0-5216]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-165|reaction.ecocyc.TRANS-RXN-165]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-502|reaction.ecocyc.TRANS-RXN0-502]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MANNPISOM-RXN|reaction.ecocyc.MANNPISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-502|reaction.ecocyc.TRANS-RXN0-502]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.SORB6PDEHYDROG-RXN|reaction.ecocyc.SORB6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:CPD-15979`
- `CHEBI:58735`
- `PUBCHEM:23421200`

## Notes

(C 6)
