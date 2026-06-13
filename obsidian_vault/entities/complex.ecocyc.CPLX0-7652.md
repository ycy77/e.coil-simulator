---
entity_id: "complex.ecocyc.CPLX0-7652"
entity_type: "complex"
name: "L-rhamnose isomerase"
source_database: "EcoCyc"
source_id: "CPLX0-7652"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-rhamnose isomerase

`complex.ecocyc.CPLX0-7652`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7652`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32170|protein.P32170]]

## Enriched Summary

EcoCyc complex CPLX0-7652

## Biological Role

Catalyzes LYXISOM-RXN (reaction.ecocyc.LYXISOM-RXN), RHAMNISOM-RXN (reaction.ecocyc.RHAMNISOM-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-7652

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.LYXISOM-RXN|reaction.ecocyc.LYXISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RHAMNISOM-RXN|reaction.ecocyc.RHAMNISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P32170|protein.P32170]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7652`
- `QSPROTEOME:QS00181733`

## Notes

4*protein.P32170
