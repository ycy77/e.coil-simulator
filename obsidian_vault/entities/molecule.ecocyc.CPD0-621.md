---
entity_id: "molecule.ecocyc.CPD0-621"
entity_type: "small_molecule"
name: "iron(III)-coprogen"
source_database: "EcoCyc"
source_id: "CPD0-621"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "ferric coprogen"
---

# iron(III)-coprogen

`molecule.ecocyc.CPD0-621`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:CPD0-621`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Coprogen is a hydroxamate compound isolated from fungi and bacteria, including Penicillium species and Neurospora crassa. It is a growth factor for coprophilous fungi. Coprogen is a hydroxamate compound isolated from fungi and bacteria, including Penicillium species and Neurospora crassa. It is a growth factor for coprophilous fungi.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Annotation

Coprogen is a hydroxamate compound isolated from fungi and bacteria, including Penicillium species and Neurospora crassa. It is a growth factor for coprophilous fungi.

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-1702|reaction.ecocyc.RXN0-1702]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-297|reaction.ecocyc.TRANS-RXN-297]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1702|reaction.ecocyc.RXN0-1702]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-297|reaction.ecocyc.TRANS-RXN-297]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-11-CPLX|complex.ecocyc.ABC-11-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:CPD0-621`
- `PUBCHEM:76957149`
- `METANETX:MNXM148240`
- `CHEBI:83101`
- `BIGG:cpgn`

## Notes

(C 35)
