---
entity_id: "complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX"
entity_type: "complex"
name: "pantothenate synthetase"
source_database: "EcoCyc"
source_id: "PANTOATE-BETA-ALANINE-LIG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pantothenate synthetase

`complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PANTOATE-BETA-ALANINE-LIG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31663|protein.P31663]]

## Enriched Summary

EcoCyc complex PANTOATE-BETA-ALANINE-LIG-CPLX

## Biological Role

Catalyzes PANTOATE-BETA-ALANINE-LIG-RXN (reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex PANTOATE-BETA-ALANINE-LIG-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN|reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P31663|protein.P31663]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PANTOATE-BETA-ALANINE-LIG-CPLX`
- `QSPROTEOME:QS00183297`

## Notes

2*protein.P31663
