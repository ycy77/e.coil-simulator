---
entity_id: "complex.ecocyc.NAG6PDEACET-CPLX"
entity_type: "complex"
name: "N-acetylglucosamine-6-phosphate deacetylase"
source_database: "EcoCyc"
source_id: "NAG6PDEACET-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# N-acetylglucosamine-6-phosphate deacetylase

`complex.ecocyc.NAG6PDEACET-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NAG6PDEACET-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AF18|protein.P0AF18]]

## Enriched Summary

EcoCyc complex NAG6PDEACET-CPLX

## Biological Role

Catalyzes NAG6PDEACET-RXN (reaction.ecocyc.NAG6PDEACET-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex NAG6PDEACET-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NAG6PDEACET-RXN|reaction.ecocyc.NAG6PDEACET-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AF18|protein.P0AF18]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:NAG6PDEACET-CPLX`
- `QSPROTEOME:QS00181703`

## Notes

4*protein.P0AF18
