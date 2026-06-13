---
entity_id: "complex.ecocyc.CPLX0-229"
entity_type: "complex"
name: "anaerobic ribonucleoside-triphosphate reductase activating protein"
source_database: "EcoCyc"
source_id: "CPLX0-229"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# anaerobic ribonucleoside-triphosphate reductase activating protein

`complex.ecocyc.CPLX0-229`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-229`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9N8|protein.P0A9N8]]

## Enriched Summary

EcoCyc complex CPLX0-229

## Biological Role

Catalyzes anaerobic ribonucleoside-triphosphate reductase activating enzyme (reaction.ecocyc.RNTRACTIV-RXN). Component of anaerobic nucleoside-triphosphate reductase activating system (complex.ecocyc.NRDACTMULTI-CPLX). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex CPLX0-229

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RNTRACTIV-RXN|reaction.ecocyc.RNTRACTIV-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.NRDACTMULTI-CPLX|complex.ecocyc.NRDACTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9N8|protein.P0A9N8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-229`
- `QSPROTEOME:QS00049400`

## Notes

2*protein.P0A9N8
