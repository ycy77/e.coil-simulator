---
entity_id: "complex.ecocyc.DCYSDESULF-CPLX"
entity_type: "complex"
name: "D-cysteine desulfhydrase, PLP-dependent / 3-chloro-D-alanine dehydrochlorinase"
source_database: "EcoCyc"
source_id: "DCYSDESULF-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-cysteine desulfhydrase, PLP-dependent / 3-chloro-D-alanine dehydrochlorinase

`complex.ecocyc.DCYSDESULF-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DCYSDESULF-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76316|protein.P76316]]

## Enriched Summary

EcoCyc complex DCYSDESULF-CPLX

## Biological Role

Catalyzes ALADEHYDCHLORO-RXN (reaction.ecocyc.ALADEHYDCHLORO-RXN), DCYSDESULF-RXN (reaction.ecocyc.DCYSDESULF-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex DCYSDESULF-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ALADEHYDCHLORO-RXN|reaction.ecocyc.ALADEHYDCHLORO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DCYSDESULF-RXN|reaction.ecocyc.DCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76316|protein.P76316]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DCYSDESULF-CPLX`
- `QSPROTEOME:QS00195281`

## Notes

2*protein.P76316
