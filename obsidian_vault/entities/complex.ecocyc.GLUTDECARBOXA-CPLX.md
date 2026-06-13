---
entity_id: "complex.ecocyc.GLUTDECARBOXA-CPLX"
entity_type: "complex"
name: "glutamate decarboxylase A"
source_database: "EcoCyc"
source_id: "GLUTDECARBOXA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate decarboxylase A

`complex.ecocyc.GLUTDECARBOXA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTDECARBOXA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69908|protein.P69908]]

## Enriched Summary

EcoCyc complex GLUTDECARBOXA-CPLX

## Biological Role

Catalyzes GLUTDECARBOX-RXN (reaction.ecocyc.GLUTDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex GLUTDECARBOXA-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P69908|protein.P69908]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:GLUTDECARBOXA-CPLX`
- `QSPROTEOME:QS00195929`

## Notes

6*protein.P69908
