---
entity_id: "complex.ecocyc.CPLX0-7687"
entity_type: "complex"
name: "succinate semialdehyde dehydrogenase (NAD(P)+) Sad"
source_database: "EcoCyc"
source_id: "CPLX0-7687"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# succinate semialdehyde dehydrogenase (NAD(P)+) Sad

`complex.ecocyc.CPLX0-7687`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7687`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76149|protein.P76149]]

## Enriched Summary

EcoCyc complex CPLX0-7687

## Biological Role

Catalyzes RXN-8182 (reaction.ecocyc.RXN-8182), SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN (reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN).

## Annotation

EcoCyc complex CPLX0-7687

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-8182|reaction.ecocyc.RXN-8182]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76149|protein.P76149]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7687`
- `QSPROTEOME:QS00049640`

## Notes

2*protein.P76149
