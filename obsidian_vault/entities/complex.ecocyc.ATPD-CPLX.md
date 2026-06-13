---
entity_id: "complex.ecocyc.ATPD-CPLX"
entity_type: "complex"
name: "ATP synthase F1 complex subunit β"
source_database: "EcoCyc"
source_id: "ATPD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP synthase F1 complex subunit β

`complex.ecocyc.ATPD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATPD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABB4|protein.P0ABB4]]

## Enriched Summary

The β subunit contains the catalytic site. The complex is a homotrimer . The role of conserved residues surrounding the catalytic site has been studied . The β subunit contains the catalytic site. The complex is a homotrimer . The role of conserved residues surrounding the catalytic site has been studied .

## Biological Role

Component of ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Annotation

The β subunit contains the catalytic site. The complex is a homotrimer . The role of conserved residues surrounding the catalytic site has been studied .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABB4|protein.P0ABB4]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:ATPD-CPLX`
- `QSPROTEOME:QS00049353`

## Notes

3*protein.P0ABB4
