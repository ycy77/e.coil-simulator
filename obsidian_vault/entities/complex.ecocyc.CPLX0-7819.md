---
entity_id: "complex.ecocyc.CPLX0-7819"
entity_type: "complex"
name: "K+ : H+ antiporter KefC"
source_database: "EcoCyc"
source_id: "CPLX0-7819"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "KefC potassium CPA2 transporter"
---

# K+ : H+ antiporter KefC

`complex.ecocyc.CPLX0-7819`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7819`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P03819|protein.P03819]]

## Enriched Summary

EcoCyc complex CPLX0-7819

## Biological Role

Catalyzes potassium:proton antiport (reaction.ecocyc.TRANS-RXN-42).

## Annotation

EcoCyc complex CPLX0-7819

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-42|reaction.ecocyc.TRANS-RXN-42]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P03819|protein.P03819]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7819`
- `QSPROTEOME:QS00203729`
- `PDB:3L9W`
- `PDB:3L9X`
- `PDB:3EYW`

## Notes

2*protein.P03819
