---
entity_id: "complex.ecocyc.CPLX0-7807"
entity_type: "complex"
name: "putative multidrug efflux pump MdtNOP"
source_database: "EcoCyc"
source_id: "CPLX0-7807"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative multidrug efflux pump MdtNOP

`complex.ecocyc.CPLX0-7807`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7807`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32714|protein.P32714]], [[protein.P32715|protein.P32715]], [[protein.P32716|protein.P32716]]

## Enriched Summary

MdtNOP is a putative multidrug efflux pump implicated in the resistance to sulfonamide antibiotics . An E. coli mdtN null mutant is more sensitive to sulfonamide antibiotics than wild type . MdtNOP is a putative multidrug efflux pump implicated in the resistance to sulfonamide antibiotics . An E. coli mdtN null mutant is more sensitive to sulfonamide antibiotics than wild type .

## Biological Role

Catalyzes sulfadiazine export (reaction.ecocyc.TRANS-RXN-351). Transports sulfadiazine (molecule.ecocyc.CPD-20940), hν (molecule.ecocyc.Light).

## Annotation

MdtNOP is a putative multidrug efflux pump implicated in the resistance to sulfonamide antibiotics . An E. coli mdtN null mutant is more sensitive to sulfonamide antibiotics than wild type .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-351|reaction.ecocyc.TRANS-RXN-351]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-20940|molecule.ecocyc.CPD-20940]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P32714|protein.P32714]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P32715|protein.P32715]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P32716|protein.P32716]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-7807`
- `QSPROTEOME:QS00185217`

## Notes

protein.P32714|protein.P32715|protein.P32716
