---
entity_id: "complex.ecocyc.CPLX0-7629"
entity_type: "complex"
name: "Na+:H+ antiporter NhaA"
source_database: "EcoCyc"
source_id: "CPLX0-7629"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Na+:H+ antiporter NhaA

`complex.ecocyc.CPLX0-7629`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7629`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P13738|protein.P13738]]

## Enriched Summary

EcoCyc complex CPLX0-7629

## Biological Role

Catalyzes electrogenic sodium:proton antiport (reaction.ecocyc.TRANS-RXN-129), Li+:proton antiport (reaction.ecocyc.TRANS-RXN-292). Transports Li+ (molecule.ecocyc.LI_).

## Annotation

EcoCyc complex CPLX0-7629

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-129|reaction.ecocyc.TRANS-RXN-129]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-292|reaction.ecocyc.TRANS-RXN-292]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P13738|protein.P13738]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7629`
- `QSPROTEOME:QS00188879`
- `PDB:1zcd`

## Notes

2*protein.P13738
