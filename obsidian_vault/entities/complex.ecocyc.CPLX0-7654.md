---
entity_id: "complex.ecocyc.CPLX0-7654"
entity_type: "complex"
name: "glycerol facilitator"
source_database: "EcoCyc"
source_id: "CPLX0-7654"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GlpF glycerol MIP channel"
---

# glycerol facilitator

`complex.ecocyc.CPLX0-7654`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7654`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P0AER0|protein.P0AER0]]

## Enriched Summary

EcoCyc complex CPLX0-7654

## Biological Role

Catalyzes RXN0-7189 (reaction.ecocyc.RXN0-7189), RXN0-7191 (reaction.ecocyc.RXN0-7191), TRANS-RXN-131 (reaction.ecocyc.TRANS-RXN-131), TRANS-RXN0-460 (reaction.ecocyc.TRANS-RXN0-460), TRANS-RXN0-536 (reaction.ecocyc.TRANS-RXN0-536), TRANS-RXN0-537 (reaction.ecocyc.TRANS-RXN0-537), TRANS-RXN0-551 (reaction.ecocyc.TRANS-RXN0-551).

## Annotation

EcoCyc complex CPLX0-7654

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7189|reaction.ecocyc.RXN0-7189]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7191|reaction.ecocyc.RXN0-7191]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-131|reaction.ecocyc.TRANS-RXN-131]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-460|reaction.ecocyc.TRANS-RXN0-460]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-536|reaction.ecocyc.TRANS-RXN0-536]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-537|reaction.ecocyc.TRANS-RXN0-537]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-551|reaction.ecocyc.TRANS-RXN0-551]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AER0|protein.P0AER0]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4 | EcoCyc transporter component coefficient=4

## External IDs

- `EcoCyc:CPLX0-7654`
- `QSPROTEOME:QS00196201`

## Notes

4*protein.P0AER0
