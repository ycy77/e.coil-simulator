---
entity_id: "complex.ecocyc.NAG1P-URIDYLTRANS-CPLX"
entity_type: "complex"
name: "fused N-acetylglucosamine-1-phosphate uridyltransferase and glucosamine-1-phosphate acetyltransferase"
source_database: "EcoCyc"
source_id: "NAG1P-URIDYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fused N-acetylglucosamine-1-phosphate uridyltransferase and glucosamine-1-phosphate acetyltransferase

`complex.ecocyc.NAG1P-URIDYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NAG1P-URIDYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ACC7|protein.P0ACC7]]

## Enriched Summary

EcoCyc complex NAG1P-URIDYLTRANS-CPLX

## Biological Role

Catalyzes 2.3.1.157-RXN (reaction.ecocyc.2.3.1.157-RXN), NAG1P-URIDYLTRANS-RXN (reaction.ecocyc.NAG1P-URIDYLTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex NAG1P-URIDYLTRANS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.3.1.157-RXN|reaction.ecocyc.2.3.1.157-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.NAG1P-URIDYLTRANS-RXN|reaction.ecocyc.NAG1P-URIDYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ACC7|protein.P0ACC7]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:NAG1P-URIDYLTRANS-CPLX`
- `QSPROTEOME:QS00158517`

## Notes

3*protein.P0ACC7
