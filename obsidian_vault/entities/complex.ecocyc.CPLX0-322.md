---
entity_id: "complex.ecocyc.CPLX0-322"
entity_type: "complex"
name: "inosine/guanosine kinase"
source_database: "EcoCyc"
source_id: "CPLX0-322"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "guanosine-inosine kinase"
  - "guanosine kinase"
---

# inosine/guanosine kinase

`complex.ecocyc.CPLX0-322`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-322`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEW6|protein.P0AEW6]]

## Enriched Summary

EcoCyc complex CPLX0-322

## Biological Role

Catalyzes GUANOSINEKIN-RXN (reaction.ecocyc.GUANOSINEKIN-RXN), INOSINEKIN-RXN (reaction.ecocyc.INOSINEKIN-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-322

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.INOSINEKIN-RXN|reaction.ecocyc.INOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEW6|protein.P0AEW6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-322`
- `QSPROTEOME:QS00200469`

## Notes

2*protein.P0AEW6
