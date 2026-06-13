---
entity_id: "complex.ecocyc.ABC-27-CPLX"
entity_type: "complex"
name: "phosphate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-27-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "pstSCAB"
---

# phosphate ABC transporter

`complex.ecocyc.ABC-27-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-27-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAH0|protein.P0AAH0]], [[protein.P07654|protein.P07654]], [[protein.P0AGH8|protein.P0AGH8]], [[protein.P0AG82|protein.P0AG82]]

## Enriched Summary

PstSCAB is an ATP-dependent phosphate uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early studies described a high affinity, binding protein dependent, phosphate (Pi) specific transport (Pst) system in E. coli that is induced in response to phosphate starvation (and see ). PstS is the periplasmic phosphate binding protein, PstA and PstC are the inner membrane subunits and PstB is the ATP-binding subunit of the transport system . The pst operon consists of five genes - pstSCAB and EG10735 "phoU" and is a member of the Pho regulon; expression is induced by phosphate limitation via the PhoRB two component system; both PstSCAB and PhoU have been implicated in phosphate signaling to PhoR (see ). PstB interacts directly with PhoU and both proteins act together in signal transduction to PhoR; regulation of alkaline phosphatase expression is perturbed in ΔpstSCABphoU, ΔpstSCAB and ΔphoU strains . The role of the Pst system in arsenate transport has been studied . Reviews: PstSCAB is an ATP-dependent phosphate uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early studies described a high affinity, binding protein dependent, phosphate (Pi) specific transport (Pst) system in E. coli that is induced in response to phosphate starvation (and see )...

## Biological Role

Catalyzes ABC-27-RXN (reaction.ecocyc.ABC-27-RXN), RXN-22326 (reaction.ecocyc.RXN-22326). Transports arsenate (molecule.ecocyc.ARSENATE), hν (molecule.ecocyc.Light).

## Annotation

PstSCAB is an ATP-dependent phosphate uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early studies described a high affinity, binding protein dependent, phosphate (Pi) specific transport (Pst) system in E. coli that is induced in response to phosphate starvation (and see ). PstS is the periplasmic phosphate binding protein, PstA and PstC are the inner membrane subunits and PstB is the ATP-binding subunit of the transport system . The pst operon consists of five genes - pstSCAB and EG10735 "phoU" and is a member of the Pho regulon; expression is induced by phosphate limitation via the PhoRB two component system; both PstSCAB and PhoU have been implicated in phosphate signaling to PhoR (see ). PstB interacts directly with PhoU and both proteins act together in signal transduction to PhoR; regulation of alkaline phosphatase expression is perturbed in ΔpstSCABphoU, ΔpstSCAB and ΔphoU strains . The role of the Pst system in arsenate transport has been studied . Reviews:

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ABC-27-RXN|reaction.ecocyc.ABC-27-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22326|reaction.ecocyc.RXN-22326]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P07654|protein.P07654]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AAH0|protein.P0AAH0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0AG82|protein.P0AG82]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGH8|protein.P0AGH8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-27-CPLX`
- `QSPROTEOME:QS00049313`

## Notes

2*protein.P0AAH0|1*protein.P07654|1*protein.P0AGH8|1*protein.P0AG82
