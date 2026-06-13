---
entity_id: "complex.ecocyc.CPLX0-7704"
entity_type: "complex"
name: "ATP-dependent Lipid A-core flippase"
source_database: "EcoCyc"
source_id: "CPLX0-7704"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Lipid A-core floppase"
---

# ATP-dependent Lipid A-core flippase

`complex.ecocyc.CPLX0-7704`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7704`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60752|protein.P60752]]

## Enriched Summary

EcoCyc complex CPLX0-7704

## Biological Role

Catalyzes TRANS-RXN-236 (reaction.ecocyc.TRANS-RXN-236), TRANS-RXN-498 (reaction.ecocyc.TRANS-RXN-498). Transports lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359), a lipid A-core oligosaccharide (molecule.ecocyc.LOS), hν (molecule.ecocyc.Light). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7704

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-236|reaction.ecocyc.TRANS-RXN-236]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-498|reaction.ecocyc.TRANS-RXN-498]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.LOS|molecule.ecocyc.LOS]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P60752|protein.P60752]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7704`
- `QSPROTEOME:QS00093466`
- `PDB:5TTP`
- `PDB:5TV4`

## Notes

2*protein.P60752
