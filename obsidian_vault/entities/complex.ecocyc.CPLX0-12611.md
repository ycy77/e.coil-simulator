---
entity_id: "complex.ecocyc.CPLX0-12611"
entity_type: "complex"
name: "molybdopterin synthase adenylyltransferase/sulfur transferase"
source_database: "EcoCyc"
source_id: "CPLX0-12611"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# molybdopterin synthase adenylyltransferase/sulfur transferase

`complex.ecocyc.CPLX0-12611`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12611`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P30748|protein.P30748]], [[complex.ecocyc.CPLX0-8164|complex.ecocyc.CPLX0-8164]]

## Enriched Summary

EcoCyc complex CPLX0-12611

## Biological Role

Catalyzes RXN-11361 (reaction.ecocyc.RXN-11361), RXN-12473 (reaction.ecocyc.RXN-12473).

## Annotation

EcoCyc complex CPLX0-12611

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11361|reaction.ecocyc.RXN-11361]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12473|reaction.ecocyc.RXN-12473]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-8164|complex.ecocyc.CPLX0-8164]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P12282|protein.P12282]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P30748|protein.P30748]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-12611`
- `PDB:1JW9`
- `PDB:1JWA`
- `PDB:1JWB`
- `QSPROTEOME:QS00191129`

## Notes

2*protein.P30748|complex.ecocyc.CPLX0-8164
