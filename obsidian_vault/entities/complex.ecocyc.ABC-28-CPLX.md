---
entity_id: "complex.ecocyc.ABC-28-CPLX"
entity_type: "complex"
name: "ribose ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-28-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribose ABC transporter

`complex.ecocyc.ABC-28-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-28-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P04983|protein.P04983]], [[protein.P0AGI1|protein.P0AGI1]], [[protein.P02925|protein.P02925]]

## Enriched Summary

RbsACB is a high affinity ribose uptake system that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Early studies characterized mutants that were defective in a high-affinity ribose transport system and characterized genes of the rbs region including rbsB, rbsA and rbsC which encode a periplasmic ribose binding protein (RbsB) , a putative ATP-binding subunit (RbsA) and a putative inner membrane protein (RbsC) . Active RbsAC2B complexes have been reconstituted in liposomes; RbsAC2B, RbsAC and RbsBC complexes can be purified by varying cofactor additions and are suggestive of a transport cycle with the following characteristics: RbsA-ATP-Mg2+ binds to ribose loaded RbsBC; ATP hydrolysis results in ribose release and dissociation of RbsB from RbsAC; ADP dissociation from RbsAC causes RbsA to dissociate which allows loaded RbsB to again bind RbsC . rbsACB is part of a larger operon - rbsDACBKR - which includes both regulatory and structural genes involved in ribose utilization; expression is subject to glucose repression mediated by CRP-cAMP; expression is negatively regulated by the the transcription factor PD03867 "RbsR" RbsACB is a high affinity ribose uptake system that is a member of the ATP-binding cassette (ABC) superfamily of transporters...

## Biological Role

Catalyzes ABC-28-RXN (reaction.ecocyc.ABC-28-RXN). Transports D-ribopyranose (molecule.ecocyc.D-Ribopyranose), hν (molecule.ecocyc.Light).

## Annotation

RbsACB is a high affinity ribose uptake system that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Early studies characterized mutants that were defective in a high-affinity ribose transport system and characterized genes of the rbs region including rbsB, rbsA and rbsC which encode a periplasmic ribose binding protein (RbsB) , a putative ATP-binding subunit (RbsA) and a putative inner membrane protein (RbsC) . Active RbsAC2B complexes have been reconstituted in liposomes; RbsAC2B, RbsAC and RbsBC complexes can be purified by varying cofactor additions and are suggestive of a transport cycle with the following characteristics: RbsA-ATP-Mg2+ binds to ribose loaded RbsBC; ATP hydrolysis results in ribose release and dissociation of RbsB from RbsAC; ADP dissociation from RbsAC causes RbsA to dissociate which allows loaded RbsB to again bind RbsC . rbsACB is part of a larger operon - rbsDACBKR - which includes both regulatory and structural genes involved in ribose utilization; expression is subject to glucose repression mediated by CRP-cAMP; expression is negatively regulated by the the transcription factor PD03867 "RbsR"

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-28-RXN|reaction.ecocyc.ABC-28-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.D-Ribopyranose|molecule.ecocyc.D-Ribopyranose]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P02925|protein.P02925]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P04983|protein.P04983]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGI1|protein.P0AGI1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-28-CPLX`
- `QSPROTEOME:QS00049314`

## Notes

1*protein.P04983|2*protein.P0AGI1|1*protein.P02925
