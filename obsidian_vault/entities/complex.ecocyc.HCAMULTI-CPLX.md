---
entity_id: "complex.ecocyc.HCAMULTI-CPLX"
entity_type: "complex"
name: "putative 3-phenylpropionate/cinnamate dioxygenase"
source_database: "EcoCyc"
source_id: "HCAMULTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "3-phenylpropionate dioxygenase complex"
  - "3-phenylpropionate dioxygenase system"
---

# putative 3-phenylpropionate/cinnamate dioxygenase

`complex.ecocyc.HCAMULTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HCAMULTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABW0|protein.P0ABW0]], [[protein.P77650|protein.P77650]], [[protein.Q47140|protein.Q47140]], [[protein.P0ABR5|protein.P0ABR5]]

## Enriched Summary

The 3-phenylpropionate dioxygenase system is predicted to be encoded by the hcaCDEF genes . 3-phenylpropionate dioxygenase has not been biochemically characterized. The 3-phenylpropionate dioxygenase system is predicted to be encoded by the hcaCDEF genes . 3-phenylpropionate dioxygenase has not been biochemically characterized.

## Biological Role

Catalyzes HCAMULTI-RXN (reaction.ecocyc.HCAMULTI-RXN), RXN-12072 (reaction.ecocyc.RXN-12072). Bound by a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

The 3-phenylpropionate dioxygenase system is predicted to be encoded by the hcaCDEF genes . 3-phenylpropionate dioxygenase has not been biochemically characterized.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.HCAMULTI-RXN|reaction.ecocyc.HCAMULTI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12072|reaction.ecocyc.RXN-12072]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABR5|protein.P0ABR5]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABW0|protein.P0ABW0]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77650|protein.P77650]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.Q47140|protein.Q47140]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:HCAMULTI-CPLX`
- `QSPROTEOME:QS00049502`

## Notes

protein.P0ABW0|protein.P77650|protein.Q47140|protein.P0ABR5
