---
entity_id: "complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX"
entity_type: "complex"
name: "acetyl-CoA acetyltransferase"
source_database: "EcoCyc"
source_id: "ACETYL-COA-ACETYLTRANSFER-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetyl-CoA acetyltransferase

`complex.ecocyc.ACETYL-COA-ACETYLTRANSFER-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETYL-COA-ACETYLTRANSFER-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76461|protein.P76461]]

## Enriched Summary

EcoCyc complex ACETYL-COA-ACETYLTRANSFER-CPLX

## Biological Role

Catalyzes ACETYL-COA-ACETYLTRANSFER-RXN (reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN).

## Annotation

EcoCyc complex ACETYL-COA-ACETYLTRANSFER-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76461|protein.P76461]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ACETYL-COA-ACETYLTRANSFER-CPLX`
- `QSPROTEOME:QS00183167`

## Notes

4*protein.P76461
