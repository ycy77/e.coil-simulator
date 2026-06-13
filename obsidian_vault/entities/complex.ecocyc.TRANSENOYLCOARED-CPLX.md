---
entity_id: "complex.ecocyc.TRANSENOYLCOARED-CPLX"
entity_type: "complex"
name: "trans-2-enoyl-CoA reductase"
source_database: "EcoCyc"
source_id: "TRANSENOYLCOARED-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# trans-2-enoyl-CoA reductase

`complex.ecocyc.TRANSENOYLCOARED-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANSENOYLCOARED-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.ecocyc.TRANSENOYLCOARED-MONOMER|protein.ecocyc.TRANSENOYLCOARED-MONOMER]]

## Enriched Summary

EcoCyc complex TRANSENOYLCOARED-CPLX

## Biological Role

Catalyzes TRANSENOYLCOARED-RXN (reaction.ecocyc.TRANSENOYLCOARED-RXN).

## Annotation

EcoCyc complex TRANSENOYLCOARED-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANSENOYLCOARED-RXN|reaction.ecocyc.TRANSENOYLCOARED-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.ecocyc.TRANSENOYLCOARED-MONOMER|protein.ecocyc.TRANSENOYLCOARED-MONOMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRANSENOYLCOARED-CPLX`

## Notes

2*protein.ecocyc.TRANSENOYLCOARED-MONOMER
