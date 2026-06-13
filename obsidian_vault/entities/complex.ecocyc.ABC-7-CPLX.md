---
entity_id: "complex.ecocyc.ABC-7-CPLX"
entity_type: "complex"
name: "thiosulfate/sulfate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-7-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thiosulfate/sulfate ABC transporter

`complex.ecocyc.ABC-7-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-7-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16676|protein.P16676]], [[protein.P0AEB0|protein.P0AEB0]], [[protein.P16701|protein.P16701]], [[protein.P16700|protein.P16700]]

## Enriched Summary

CysPUWA is an ATP-dependent, high affinity thiosulfate/sulfate uptake system that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. cysU, cysW and cysA encode the integral membrane proteins (CysU and CysW) and ATP-binding subunit (CysA) of a transporter complex that interacts separately with two periplasmic binding proteins - CysP and SBP-MONOMER "Sbp - to mediate the high affinity uptake of sulfate and thiosulfate . Double cysP sbp mutants (cysP::Cat sbp::Kan) are cysteine auxotrophs; growth on sulfate (and thiosulfate) as sole sulfur source can be restored in the double mutant by multicopy expression of either cysP or sbp however growth is impaired compared to the wild type strain; CysP and Sbp have overlapping specificity and both are required for wild-type levels of sulfate/thiosulfate transport . The CysPUWA-Sbp transport system acts as an alternate molybdate transport system although it is not clear whether it is used only in the absence of a functional molybdate specific system (ABC-19-CPLX "ModABC") . Additionally, kinetic analyses indicate that sulphate, selenate and selenite are all transported by the same system in E. coli K-12 (and see ). The role of the two periplasmic binding proteins, Sbp and/or CysP, in transporting these alternate substrates is not defined...

## Biological Role

Catalyzes ABC-19-RXN (reaction.ecocyc.ABC-19-RXN), ABC-7-RXN (reaction.ecocyc.ABC-7-RXN), ABC-70-RXN (reaction.ecocyc.ABC-70-RXN), TRANS-RXN0-478 (reaction.ecocyc.TRANS-RXN0-478), TRANS-RXN0-479 (reaction.ecocyc.TRANS-RXN0-479). Transports Sulfate (molecule.C00059), Selenite (molecule.C05684), Selenate (molecule.C05697), Molybdate (molecule.C06232), hν (molecule.ecocyc.Light).

## Annotation

CysPUWA is an ATP-dependent, high affinity thiosulfate/sulfate uptake system that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. cysU, cysW and cysA encode the integral membrane proteins (CysU and CysW) and ATP-binding subunit (CysA) of a transporter complex that interacts separately with two periplasmic binding proteins - CysP and SBP-MONOMER "Sbp - to mediate the high affinity uptake of sulfate and thiosulfate . Double cysP sbp mutants (cysP::Cat sbp::Kan) are cysteine auxotrophs; growth on sulfate (and thiosulfate) as sole sulfur source can be restored in the double mutant by multicopy expression of either cysP or sbp however growth is impaired compared to the wild type strain; CysP and Sbp have overlapping specificity and both are required for wild-type levels of sulfate/thiosulfate transport . The CysPUWA-Sbp transport system acts as an alternate molybdate transport system although it is not clear whether it is used only in the absence of a functional molybdate specific system (ABC-19-CPLX "ModABC") . Additionally, kinetic analyses indicate that sulphate, selenate and selenite are all transported by the same system in E. coli K-12 (and see ). The role of the two periplasmic binding proteins, Sbp and/or CysP, in transporting these alternate substrates is not defined. Review:

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.ecocyc.ABC-19-RXN|reaction.ecocyc.ABC-19-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-7-RXN|reaction.ecocyc.ABC-7-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-70-RXN|reaction.ecocyc.ABC-70-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-478|reaction.ecocyc.TRANS-RXN0-478]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-479|reaction.ecocyc.TRANS-RXN0-479]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05684|molecule.C05684]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05697|molecule.C05697]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C06232|molecule.C06232]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AEB0|protein.P0AEB0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P16676|protein.P16676]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P16700|protein.P16700]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P16701|protein.P16701]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-7-CPLX`
- `QSPROTEOME:QS00049295`

## Notes

2*protein.P16676|1*protein.P0AEB0|1*protein.P16701|1*protein.P16700
