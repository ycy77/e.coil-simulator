---
entity_id: "complex.ecocyc.ALAS-CPLX"
entity_type: "complex"
name: "alanine—tRNA ligase/DNA-binding transcriptional repressor"
source_database: "EcoCyc"
source_id: "ALAS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# alanine—tRNA ligase/DNA-binding transcriptional repressor

`complex.ecocyc.ALAS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ALAS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00957|protein.P00957]]

## Enriched Summary

EcoCyc complex ALAS-CPLX

## Biological Role

Catalyzes ALANINE--TRNA-LIGASE-RXN (reaction.ecocyc.ALANINE--TRNA-LIGASE-RXN), RXN-19726 (reaction.ecocyc.RXN-19726), RXN-23938 (reaction.ecocyc.RXN-23938), RXN-23960 (reaction.ecocyc.RXN-23960), RXN-23961 (reaction.ecocyc.RXN-23961). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex ALAS-CPLX

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ALANINE--TRNA-LIGASE-RXN|reaction.ecocyc.ALANINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19726|reaction.ecocyc.RXN-19726]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23938|reaction.ecocyc.RXN-23938]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23960|reaction.ecocyc.RXN-23960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23961|reaction.ecocyc.RXN-23961]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00957|protein.P00957]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ALAS-CPLX`
- `QSPROTEOME:QS00049544`

## Notes

2*protein.P00957
