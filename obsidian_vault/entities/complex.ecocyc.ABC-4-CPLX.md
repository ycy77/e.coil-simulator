---
entity_id: "complex.ecocyc.ABC-4-CPLX"
entity_type: "complex"
name: "L-arginine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-4-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-arginine ABC transporter

`complex.ecocyc.ABC-4-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-4-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P30860|protein.P30860]], [[protein.P0AE34|protein.P0AE34]], [[protein.P0AE30|protein.P0AE30]], [[protein.P0AAF6|protein.P0AAF6]]

## Enriched Summary

ArtPQMJ is an L-arginine transporter that is a member of the ATP Binding Cassette (ABC) superfamily . Sequence analysis indicates that ArtQ and ArtM are the integral membrane components and ArtP forms the ATP binding domain. ArtJ is a periplasmic binding protein with high affinity for L-arginine . The art gene cluster contains two transcription units: artPIQM and artJ which are regulated by the the arginine repressor, CPLX0-228 "ArgR" . ArtI exhibits homology with a number of ABC transporter periplasmic binding proteins, but its substrate is not known . Purified ArtI does not bind any of the common or uncommon amino acids or putrescine . ArtPQMJ is an L-arginine transporter that is a member of the ATP Binding Cassette (ABC) superfamily . Sequence analysis indicates that ArtQ and ArtM are the integral membrane components and ArtP forms the ATP binding domain. ArtJ is a periplasmic binding protein with high affinity for L-arginine . The art gene cluster contains two transcription units: artPIQM and artJ which are regulated by the the arginine repressor, CPLX0-228 "ArgR" . ArtI exhibits homology with a number of ABC transporter periplasmic binding proteins, but its substrate is not known . Purified ArtI does not bind any of the common or uncommon amino acids or putrescine .

## Biological Role

Catalyzes ABC-4-RXN (reaction.ecocyc.ABC-4-RXN). Transports L-Arginine (molecule.C00062), hν (molecule.ecocyc.Light).

## Annotation

ArtPQMJ is an L-arginine transporter that is a member of the ATP Binding Cassette (ABC) superfamily . Sequence analysis indicates that ArtQ and ArtM are the integral membrane components and ArtP forms the ATP binding domain. ArtJ is a periplasmic binding protein with high affinity for L-arginine . The art gene cluster contains two transcription units: artPIQM and artJ which are regulated by the the arginine repressor, CPLX0-228 "ArgR" . ArtI exhibits homology with a number of ABC transporter periplasmic binding proteins, but its substrate is not known . Purified ArtI does not bind any of the common or uncommon amino acids or putrescine .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-4-RXN|reaction.ecocyc.ABC-4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AAF6|protein.P0AAF6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0AE30|protein.P0AE30]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AE34|protein.P0AE34]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P30860|protein.P30860]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-4-CPLX`
- `QSPROTEOME:QS00049293`

## Notes

1*protein.P30860|1*protein.P0AE34|1*protein.P0AE30|2*protein.P0AAF6
