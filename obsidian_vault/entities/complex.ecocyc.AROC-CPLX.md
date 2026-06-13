---
entity_id: "complex.ecocyc.AROC-CPLX"
entity_type: "complex"
name: "chorismate synthase"
source_database: "EcoCyc"
source_id: "AROC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# chorismate synthase

`complex.ecocyc.AROC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AROC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P12008|protein.P12008]]

## Enriched Summary

EcoCyc complex AROC-CPLX

## Biological Role

Catalyzes CHORISMATE-SYNTHASE-RXN (reaction.ecocyc.CHORISMATE-SYNTHASE-RXN). Bound by Reduced FMN (molecule.C01847).

## Annotation

EcoCyc complex AROC-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CHORISMATE-SYNTHASE-RXN|reaction.ecocyc.CHORISMATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P12008|protein.P12008]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:AROC-CPLX`
- `QSPROTEOME:QS00049568`

## Notes

4*protein.P12008
