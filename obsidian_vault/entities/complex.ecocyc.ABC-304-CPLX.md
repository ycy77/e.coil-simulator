---
entity_id: "complex.ecocyc.ABC-304-CPLX"
entity_type: "complex"
name: "leucine / L-phenylalanine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-304-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# leucine / L-phenylalanine ABC transporter

`complex.ecocyc.ABC-304-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-304-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P04816|protein.P04816]], [[protein.P22729|protein.P22729]], [[protein.P0AEX7|protein.P0AEX7]], [[protein.P0A9S7|protein.P0A9S7]], [[protein.P22731|protein.P22731]]

## Enriched Summary

LivKHMGF is an ATP-dependent high-affinity leucine transport system, also known as the LS or leucine specific system, that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Early studies identified two high affinity, binding protein dependent, leucine uptake sysems in E. coli K-12: LS, a high affinity uptake system specific for L-leucine and ABC-15-CPLX "LIV-"I, a common transporter for L-leucine, L-isoleucine and L-valine . Later studies suggested that the LS system also transports L-isoleucine and L-valine (with Km values of 5 and 9.2 µM respectively) . The LS system is also able to transport phenylanine and the LIV-I / LS system plays a physiologically relevant role in phenylalanine accumulation in E. coli cells. The LS system is able to transport both isomers of leucine . The two systems share membrane and ATP-binding components but have distinctive periplasmic binding proteins. LivF and LivG are the ATP-binding components of the transporter complex, LivH and LivM are the integral membrane proteins. LivK is the periplasmic binding protein associated with the LS system and LivJ is the periplasmic binding protein associated with the LIV-I system...

## Biological Role

Catalyzes ABC-35-RXN (reaction.ecocyc.ABC-35-RXN), TRANS-RXN-312 (reaction.ecocyc.TRANS-RXN-312). Transports (3R)-β-phenylalanine (molecule.ecocyc.CPD-14474), hν (molecule.ecocyc.Light).

## Annotation

LivKHMGF is an ATP-dependent high-affinity leucine transport system, also known as the LS or leucine specific system, that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Early studies identified two high affinity, binding protein dependent, leucine uptake sysems in E. coli K-12: LS, a high affinity uptake system specific for L-leucine and ABC-15-CPLX "LIV-"I, a common transporter for L-leucine, L-isoleucine and L-valine . Later studies suggested that the LS system also transports L-isoleucine and L-valine (with Km values of 5 and 9.2 µM respectively) . The LS system is also able to transport phenylanine and the LIV-I / LS system plays a physiologically relevant role in phenylalanine accumulation in E. coli cells. The LS system is able to transport both isomers of leucine . The two systems share membrane and ATP-binding components but have distinctive periplasmic binding proteins. LivF and LivG are the ATP-binding components of the transporter complex, LivH and LivM are the integral membrane proteins. LivK is the periplasmic binding protein associated with the LS system and LivJ is the periplasmic binding protein associated with the LIV-I system . A strain lacking livK and livJ and unable to express livHMGF is unable to carry out high-affinity transport of leucine; expression of livHMGF and either of the binding protein genes (livK,livJ) from a plasmid restores high affinity leucine transport . The liv genes are divided into two transcription units, one for livJ and the other for livKHMGF; expression is repressed by Lrp in the presence of leucine . liv: leucine isoleucine valine

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ABC-35-RXN|reaction.ecocyc.ABC-35-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-312|reaction.ecocyc.TRANS-RXN-312]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-14474|molecule.ecocyc.CPD-14474]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P04816|protein.P04816]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0A9S7|protein.P0A9S7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEX7|protein.P0AEX7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P22729|protein.P22729]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P22731|protein.P22731]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-304-CPLX`
- `QSPROTEOME:QS00049341`

## Notes

1*protein.P04816|1*protein.P22729|1*protein.P0AEX7|1*protein.P0A9S7|1*protein.P22731
