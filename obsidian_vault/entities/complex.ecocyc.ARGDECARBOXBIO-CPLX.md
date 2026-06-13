---
entity_id: "complex.ecocyc.ARGDECARBOXBIO-CPLX"
entity_type: "complex"
name: "biosynthetic arginine decarboxylase"
source_database: "EcoCyc"
source_id: "ARGDECARBOXBIO-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# biosynthetic arginine decarboxylase

`complex.ecocyc.ARGDECARBOXBIO-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ARGDECARBOXBIO-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P21170|protein.P21170]]

## Enriched Summary

EcoCyc complex ARGDECARBOXBIO-CPLX

## Biological Role

Catalyzes ARGDECARBOX-RXN (reaction.ecocyc.ARGDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex ARGDECARBOXBIO-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21170|protein.P21170]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ARGDECARBOXBIO-CPLX`
- `QSPROTEOME:QS00182707`

## Notes

4*protein.P21170
