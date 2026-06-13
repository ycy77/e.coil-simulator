---
entity_id: "complex.ecocyc.ABC-2-CPLX"
entity_type: "complex"
name: "arabinose ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-2-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# arabinose ABC transporter

`complex.ecocyc.ABC-2-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-2-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P0AAF3|protein.P0AAF3]], [[protein.P0AE26|protein.P0AE26]], [[protein.P02924|protein.P02924]]

## Enriched Summary

E. coli K-12 contains two kinetically distinguishable systems for L-arabinose import - the low affinity AraE L-arabinose:H+ symporter and the high affinity ATP-driven system encoded by the araFGH genes . The AraFGH arabinose transporter is a member of the ATP Binding Cassette (ABC) transporter superfamily . Expression of all three components is necessary to complement high-affinity arabinose transport in an araFGH knockout strain . The AraF periplasmic binding protein has been experimentally characterised . Based on sequence similarity, AraH is the membrane component and AraG is the ATP-binding component of this ABC transporter . Transcription of the araFGH operon is positively regulated by the EG10054 "AraC" protein in the presence of arabinose and cAMP-CRP . E. coli K-12 contains two kinetically distinguishable systems for L-arabinose import - the low affinity AraE L-arabinose:H+ symporter and the high affinity ATP-driven system encoded by the araFGH genes . The AraFGH arabinose transporter is a member of the ATP Binding Cassette (ABC) transporter superfamily . Expression of all three components is necessary to complement high-affinity arabinose transport in an araFGH knockout strain . The AraF periplasmic binding protein has been experimentally characterised...

## Biological Role

Catalyzes ABC-2-RXN (reaction.ecocyc.ABC-2-RXN). Transports L-Arabinose (molecule.C00259), hν (molecule.ecocyc.Light).

## Annotation

E. coli K-12 contains two kinetically distinguishable systems for L-arabinose import - the low affinity AraE L-arabinose:H+ symporter and the high affinity ATP-driven system encoded by the araFGH genes . The AraFGH arabinose transporter is a member of the ATP Binding Cassette (ABC) transporter superfamily . Expression of all three components is necessary to complement high-affinity arabinose transport in an araFGH knockout strain . The AraF periplasmic binding protein has been experimentally characterised . Based on sequence similarity, AraH is the membrane component and AraG is the ATP-binding component of this ABC transporter . Transcription of the araFGH operon is positively regulated by the EG10054 "AraC" protein in the presence of arabinose and cAMP-CRP .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-2-RXN|reaction.ecocyc.ABC-2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P02924|protein.P02924]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AAF3|protein.P0AAF3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0AE26|protein.P0AE26]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-2-CPLX`
- `QSPROTEOME:QS00049291`

## Notes

2*protein.P0AAF3|2*protein.P0AE26|1*protein.P02924
