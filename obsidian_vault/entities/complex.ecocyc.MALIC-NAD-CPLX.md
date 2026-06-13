---
entity_id: "complex.ecocyc.MALIC-NAD-CPLX"
entity_type: "complex"
name: "malate dehydrogenase (oxaloacetate-decarboxylating)"
source_database: "EcoCyc"
source_id: "MALIC-NAD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# malate dehydrogenase (oxaloacetate-decarboxylating)

`complex.ecocyc.MALIC-NAD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:MALIC-NAD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P26616|protein.P26616]]

## Enriched Summary

EcoCyc complex MALIC-NAD-CPLX

## Biological Role

Catalyzes 1.1.1.39-RXN (reaction.ecocyc.1.1.1.39-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex MALIC-NAD-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P26616|protein.P26616]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:MALIC-NAD-CPLX`
- `QSPROTEOME:QS00181571`

## Notes

4*protein.P26616
