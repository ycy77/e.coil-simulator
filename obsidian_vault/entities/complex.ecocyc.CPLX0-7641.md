---
entity_id: "complex.ecocyc.CPLX0-7641"
entity_type: "complex"
name: "Zn2+/Fe2+/Cd2+ exporter"
source_database: "EcoCyc"
source_id: "CPLX0-7641"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Zn2+/Fe2+/Cd2+ exporter

`complex.ecocyc.CPLX0-7641`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7641`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P69380|protein.P69380]]

## Enriched Summary

EcoCyc complex CPLX0-7641

## Biological Role

Catalyzes Fe2+:proton antiport (reaction.ecocyc.RXN0-6), Zn2+:proton antiport (reaction.ecocyc.TRANS-RXN0-200), Cd2+:proton antiport (reaction.ecocyc.TRANS-RXN0-244). Transports Zinc cation (molecule.C00038), Fe2+ (molecule.C14818), Cd2+ (molecule.ecocyc.CD_2), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-7641

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6|reaction.ecocyc.RXN0-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-200|reaction.ecocyc.TRANS-RXN0-200]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-244|reaction.ecocyc.TRANS-RXN0-244]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P69380|protein.P69380]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7641`
- `QSPROTEOME:QS00195957`
- `PDB:2qfi`

## Notes

2*protein.P69380
