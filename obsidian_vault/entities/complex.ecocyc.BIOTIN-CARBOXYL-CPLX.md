---
entity_id: "complex.ecocyc.BIOTIN-CARBOXYL-CPLX"
entity_type: "complex"
name: "biotin carboxylase"
source_database: "EcoCyc"
source_id: "BIOTIN-CARBOXYL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# biotin carboxylase

`complex.ecocyc.BIOTIN-CARBOXYL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:BIOTIN-CARBOXYL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P24182|protein.P24182]]

## Enriched Summary

EcoCyc complex BIOTIN-CARBOXYL-CPLX

## Biological Role

Catalyzes BIOTIN-CARBOXYL-RXN (reaction.ecocyc.BIOTIN-CARBOXYL-RXN). Component of acetyl-CoA carboxylase complex (complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX).

## Annotation

EcoCyc complex BIOTIN-CARBOXYL-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.BIOTIN-CARBOXYL-RXN|reaction.ecocyc.BIOTIN-CARBOXYL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P24182|protein.P24182]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:BIOTIN-CARBOXYL-CPLX`
- `QSPROTEOME:QS00183245`

## Notes

2*protein.P24182
