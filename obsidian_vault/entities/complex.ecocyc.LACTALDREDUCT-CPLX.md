---
entity_id: "complex.ecocyc.LACTALDREDUCT-CPLX"
entity_type: "complex"
name: "lactaldehyde reductase"
source_database: "EcoCyc"
source_id: "LACTALDREDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "L-1,2-propanediol oxidoreductase"
---

# lactaldehyde reductase

`complex.ecocyc.LACTALDREDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LACTALDREDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9S1|protein.P0A9S1]]

## Enriched Summary

EcoCyc complex LACTALDREDUCT-CPLX

## Biological Role

Catalyzes GLYCOLALDREDUCT-RXN (reaction.ecocyc.GLYCOLALDREDUCT-RXN), LACTALDREDUCT-RXN (reaction.ecocyc.LACTALDREDUCT-RXN). Bound by Fe2+ (molecule.C14818).

## Annotation

EcoCyc complex LACTALDREDUCT-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLYCOLALDREDUCT-RXN|reaction.ecocyc.GLYCOLALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.LACTALDREDUCT-RXN|reaction.ecocyc.LACTALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9S1|protein.P0A9S1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:LACTALDREDUCT-CPLX`
- `QSPROTEOME:QS00195913`

## Notes

2*protein.P0A9S1
