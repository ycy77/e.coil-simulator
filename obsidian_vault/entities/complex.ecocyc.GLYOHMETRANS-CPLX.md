---
entity_id: "complex.ecocyc.GLYOHMETRANS-CPLX"
entity_type: "complex"
name: "serine hydroxymethyltransferase"
source_database: "EcoCyc"
source_id: "GLYOHMETRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# serine hydroxymethyltransferase

`complex.ecocyc.GLYOHMETRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYOHMETRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A825|protein.P0A825]]

## Enriched Summary

EcoCyc complex GLYOHMETRANS-CPLX

## Biological Role

Catalyzes DSERDEAM-RXN (reaction.ecocyc.DSERDEAM-RXN), GLYOHMETRANS-RXN (reaction.ecocyc.GLYOHMETRANS-RXN), RXN-6321 (reaction.ecocyc.RXN-6321), RXN0-5234 (reaction.ecocyc.RXN0-5234), RXN0-5240 (reaction.ecocyc.RXN0-5240). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex GLYOHMETRANS-CPLX

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.DSERDEAM-RXN|reaction.ecocyc.DSERDEAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLYOHMETRANS-RXN|reaction.ecocyc.GLYOHMETRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-6321|reaction.ecocyc.RXN-6321]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5234|reaction.ecocyc.RXN0-5234]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5240|reaction.ecocyc.RXN0-5240]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A825|protein.P0A825]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYOHMETRANS-CPLX`
- `QSPROTEOME:QS00192375`

## Notes

2*protein.P0A825
