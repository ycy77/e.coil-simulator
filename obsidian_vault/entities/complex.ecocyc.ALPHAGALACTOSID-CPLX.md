---
entity_id: "complex.ecocyc.ALPHAGALACTOSID-CPLX"
entity_type: "complex"
name: "α-galactosidase"
source_database: "EcoCyc"
source_id: "ALPHAGALACTOSID-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# α-galactosidase

`complex.ecocyc.ALPHAGALACTOSID-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ALPHAGALACTOSID-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P06720|protein.P06720]]

## Enriched Summary

EcoCyc complex ALPHAGALACTOSID-CPLX

## Biological Role

Catalyzes ALPHAGALACTOSID-RXN (reaction.ecocyc.ALPHAGALACTOSID-RXN), RXN-17754 (reaction.ecocyc.RXN-17754). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex ALPHAGALACTOSID-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ALPHAGALACTOSID-RXN|reaction.ecocyc.ALPHAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17754|reaction.ecocyc.RXN-17754]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06720|protein.P06720]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ALPHAGALACTOSID-CPLX`
- `QSPROTEOME:QS00049545`

## Notes

2*protein.P06720
