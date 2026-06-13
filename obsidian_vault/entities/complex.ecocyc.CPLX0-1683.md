---
entity_id: "complex.ecocyc.CPLX0-1683"
entity_type: "complex"
name: "adenine deaminase"
source_database: "EcoCyc"
source_id: "CPLX0-1683"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "cryptic adenine deaminase"
---

# adenine deaminase

`complex.ecocyc.CPLX0-1683`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1683`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31441|protein.P31441]]

## Enriched Summary

EcoCyc complex CPLX0-1683

## Biological Role

Catalyzes ADENINE-DEAMINASE-RXN (reaction.ecocyc.ADENINE-DEAMINASE-RXN), CATAL-RXN (reaction.ecocyc.CATAL-RXN). Bound by Fe2+ (molecule.C14818), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-1683

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ADENINE-DEAMINASE-RXN|reaction.ecocyc.ADENINE-DEAMINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CATAL-RXN|reaction.ecocyc.CATAL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P31441|protein.P31441]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1683`
- `QSPROTEOME:QS00049599`

## Notes

2*protein.P31441
