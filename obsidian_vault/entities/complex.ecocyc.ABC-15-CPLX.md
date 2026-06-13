---
entity_id: "complex.ecocyc.ABC-15-CPLX"
entity_type: "complex"
name: "branched chain amino acid / phenylalanine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-15-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "LIV-I transport system"
---

# branched chain amino acid / phenylalanine ABC transporter

`complex.ecocyc.ABC-15-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-15-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P22731|protein.P22731]], [[protein.P0A9S7|protein.P0A9S7]], [[protein.P0AEX7|protein.P0AEX7]], [[protein.P22729|protein.P22729]], [[protein.P0AD96|protein.P0AD96]]

## Enriched Summary

LivJHMGF is an ATP-dependent high-affinity branched-chain amino acid transport system, also known as the LIV-I system, that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Early studies identified two high affinity, binding protein dependent, leucine uptake sysems in E. coli K-12: LIV-I, a common transporter for L-leucine, L-isoleucine and L-valine and ABC-304-CPLX "LS", a high affinity uptake system specific for L-leucine. LIV-I was also reported to transport L-alanine, L-threonine and possibly L-serine . Later studies suggested that the LS system also transports L-isoleucine and L-valine . The LIV-I system is also able to transport phenylanine and the LIV-I / LS system plays a physiologically relevant role in phenylalanine accumulation in E. coli cells. The LIV-I system is able to transport tyrosine but not at levels that support growth of a tyrosine auxotrophic strain . The two systems share membrane and ATP-binding components but have distinctive periplasmic binding proteins. LivF and LivG are the ATP-binding components of the transporter complex, LivH and LivM are the integral membrane proteins. LivJ is the periplasmic binding protein associated with the LIV-I system and LivK is the periplasmic binding protein associated with the LS system...

## Biological Role

Catalyzes ABC-15-RXN (reaction.ecocyc.ABC-15-RXN), ABC-35-RXN (reaction.ecocyc.ABC-35-RXN), ABC-36-RXN (reaction.ecocyc.ABC-36-RXN), TRANS-RXN-312 (reaction.ecocyc.TRANS-RXN-312). Transports L-Leucine (molecule.C00123), L-Valine (molecule.C00183), L-Isoleucine (molecule.C00407), hν (molecule.ecocyc.Light).

## Annotation

LivJHMGF is an ATP-dependent high-affinity branched-chain amino acid transport system, also known as the LIV-I system, that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Early studies identified two high affinity, binding protein dependent, leucine uptake sysems in E. coli K-12: LIV-I, a common transporter for L-leucine, L-isoleucine and L-valine and ABC-304-CPLX "LS", a high affinity uptake system specific for L-leucine. LIV-I was also reported to transport L-alanine, L-threonine and possibly L-serine . Later studies suggested that the LS system also transports L-isoleucine and L-valine . The LIV-I system is also able to transport phenylanine and the LIV-I / LS system plays a physiologically relevant role in phenylalanine accumulation in E. coli cells. The LIV-I system is able to transport tyrosine but not at levels that support growth of a tyrosine auxotrophic strain . The two systems share membrane and ATP-binding components but have distinctive periplasmic binding proteins. LivF and LivG are the ATP-binding components of the transporter complex, LivH and LivM are the integral membrane proteins. LivJ is the periplasmic binding protein associated with the LIV-I system and LivK is the periplasmic binding protein associated with the LS system . A strain lacking livK and livJ and unable to express livHMGF is unable to carry out high-affinity transport of leucine; expression of livHMGF and either of the binding protein genes (livK,livJ) from a plasmid restores high affinity leucine transport . The liv genes are divided into two transcription units, one for livJ and the other for livKHMGF; expression is repressed by Lrp in the presence of leucine . liv: leucine isoleucine valine

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.ABC-15-RXN|reaction.ecocyc.ABC-15-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-35-RXN|reaction.ecocyc.ABC-35-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-36-RXN|reaction.ecocyc.ABC-36-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-312|reaction.ecocyc.TRANS-RXN-312]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0A9S7|protein.P0A9S7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AD96|protein.P0AD96]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEX7|protein.P0AEX7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P22729|protein.P22729]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P22731|protein.P22731]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-15-CPLX`
- `QSPROTEOME:QS00049303`

## Notes

1*protein.P22731|1*protein.P0A9S7|1*protein.P0AEX7|1*protein.P22729|1*protein.P0AD96
