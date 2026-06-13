---
entity_id: "complex.ecocyc.CPLX0-861"
entity_type: "complex"
name: "protein/nucleic acid deglycase 1"
source_database: "EcoCyc"
source_id: "CPLX0-861"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# protein/nucleic acid deglycase 1

`complex.ecocyc.CPLX0-861`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-861`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31658|protein.P31658]]

## Enriched Summary

EcoCyc complex CPLX0-861

## Biological Role

Catalyzes GLYOXIII-RXN (reaction.ecocyc.GLYOXIII-RXN), RXN-17630 (reaction.ecocyc.RXN-17630), RXN-17632 (reaction.ecocyc.RXN-17632), RXN-17634 (reaction.ecocyc.RXN-17634).

## Annotation

EcoCyc complex CPLX0-861

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.GLYOXIII-RXN|reaction.ecocyc.GLYOXIII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17630|reaction.ecocyc.RXN-17630]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17632|reaction.ecocyc.RXN-17632]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17634|reaction.ecocyc.RXN-17634]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31658|protein.P31658]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-861`
- `QSPROTEOME:QS00181531`

## Notes

2*protein.P31658
