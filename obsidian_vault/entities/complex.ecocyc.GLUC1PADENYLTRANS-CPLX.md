---
entity_id: "complex.ecocyc.GLUC1PADENYLTRANS-CPLX"
entity_type: "complex"
name: "glucose-1-phosphate adenylyltransferase"
source_database: "EcoCyc"
source_id: "GLUC1PADENYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glucose-1-phosphate adenylyltransferase

`complex.ecocyc.GLUC1PADENYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUC1PADENYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6V1|protein.P0A6V1]]

## Enriched Summary

EcoCyc complex GLUC1PADENYLTRANS-CPLX

## Biological Role

Catalyzes GLUC1PADENYLTRANS-RXN (reaction.ecocyc.GLUC1PADENYLTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex GLUC1PADENYLTRANS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUC1PADENYLTRANS-RXN|reaction.ecocyc.GLUC1PADENYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6V1|protein.P0A6V1]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GLUC1PADENYLTRANS-CPLX`
- `QSPROTEOME:QS00190109`

## Notes

4*protein.P0A6V1
