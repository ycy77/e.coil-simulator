---
entity_id: "molecule.ecocyc.DIPEPTIDES"
entity_type: "small_molecule"
name: "a dipeptide"
source_database: "EcoCyc"
source_id: "DIPEPTIDES"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "an aminoacyl-amino acid"
---

# a dipeptide

`molecule.ecocyc.DIPEPTIDES`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:DIPEPTIDES`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound DIPEPTIDES

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Annotation

EcoCyc compound DIPEPTIDES

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.3.4.11.4-RXN|reaction.ecocyc.3.4.11.4-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3.4.15.5-RXN|reaction.ecocyc.3.4.15.5-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ABC-8-RXN|reaction.ecocyc.ABC-8-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-288|reaction.ecocyc.TRANS-RXN0-288]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3.4.13.18-RXN|reaction.ecocyc.3.4.13.18-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-8-RXN|reaction.ecocyc.ABC-8-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-288|reaction.ecocyc.TRANS-RXN0-288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-8-CPLX|complex.ecocyc.ABC-8-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P77304|protein.P77304]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:DIPEPTIDES`
- `SEED:cpd11618`
- `METANETX:MNXM162305`
- `LIGAND-CPD:C16116`
