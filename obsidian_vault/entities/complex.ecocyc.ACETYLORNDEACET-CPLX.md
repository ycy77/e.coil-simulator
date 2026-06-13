---
entity_id: "complex.ecocyc.ACETYLORNDEACET-CPLX"
entity_type: "complex"
name: "acetylornithine deacetylase"
source_database: "EcoCyc"
source_id: "ACETYLORNDEACET-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetylornithine deacetylase

`complex.ecocyc.ACETYLORNDEACET-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETYLORNDEACET-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23908|protein.P23908]]

## Enriched Summary

EcoCyc complex ACETYLORNDEACET-CPLX

## Biological Role

Catalyzes ACETYLORNDEACET-RXN (reaction.ecocyc.ACETYLORNDEACET-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex ACETYLORNDEACET-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ACETYLORNDEACET-RXN|reaction.ecocyc.ACETYLORNDEACET-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23908|protein.P23908]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETYLORNDEACET-CPLX`
- `QSPROTEOME:QS00181859`

## Notes

2*protein.P23908
