---
entity_id: "complex.ecocyc.ABC-16-CPLX"
entity_type: "complex"
name: "maltose ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-16-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# maltose ABC transporter

`complex.ecocyc.ABC-16-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-16-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P68187|protein.P68187]], [[protein.P02916|protein.P02916]], [[protein.P68183|protein.P68183]], [[protein.P0AEX9|protein.P0AEX9]]

## Enriched Summary

MalEFGK2 is a maltose uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. MalE is the periplasmic maltose-binding protein (MBP) , MalF and MalG are the integral membrane components and MalK is the ATP-binding component of the transporter, peripherally associated with the inner membrane through its interactions with MalF and MalG . The maltose ABC transporter is capable of transporting malto-oligosaccharides up to seven glucose units long . Maltose uptake in proteoliposomes containing purified, solubilised MalF, MalG and MalK is dependent on the presence of the periplasmic MBP (MalE) and ATP . Hydrolysis of ATP is directly coupled to maltose uptake in the MalEFGK2 system . Purified MalFGK forms a complex containing 2 MalK subunits, one MalF and one MalG; MalF interacts specifically with both MalG and MalK . MalE stimulates the ATPase activity of MalFGK2; ATP hydrolysis is maximally stimulated by liganded MalE . MalE binding stabilises the transition state of the MalFGK2 complex and may facilitate transfer of maltose from the binding protein to the transporter . MalE interacts with MalF and MalG throughout the transport cycle ; a MalF periplasmic loop (MalF-P2) remains in close contact with MalE throughout the transport cycle ; MalF-P2 binds MalE in both the presence and absence of substrate...

## Biological Role

Catalyzes ABC-16-RXN (reaction.ecocyc.ABC-16-RXN), RXN0-7495 (reaction.ecocyc.RXN0-7495), TRANS-RXN0-503 (reaction.ecocyc.TRANS-RXN0-503), TRANS-RXN0-504 (reaction.ecocyc.TRANS-RXN0-504). Transports Maltose (molecule.C00208), Maltotriose (molecule.C01835), hν (molecule.ecocyc.Light), maltohexaose (molecule.ecocyc.MALTOHEXAOSE), maltotetraose (molecule.ecocyc.MALTOTETRAOSE).

## Annotation

MalEFGK2 is a maltose uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. MalE is the periplasmic maltose-binding protein (MBP) , MalF and MalG are the integral membrane components and MalK is the ATP-binding component of the transporter, peripherally associated with the inner membrane through its interactions with MalF and MalG . The maltose ABC transporter is capable of transporting malto-oligosaccharides up to seven glucose units long . Maltose uptake in proteoliposomes containing purified, solubilised MalF, MalG and MalK is dependent on the presence of the periplasmic MBP (MalE) and ATP . Hydrolysis of ATP is directly coupled to maltose uptake in the MalEFGK2 system . Purified MalFGK forms a complex containing 2 MalK subunits, one MalF and one MalG; MalF interacts specifically with both MalG and MalK . MalE stimulates the ATPase activity of MalFGK2; ATP hydrolysis is maximally stimulated by liganded MalE . MalE binding stabilises the transition state of the MalFGK2 complex and may facilitate transfer of maltose from the binding protein to the transporter . MalE interacts with MalF and MalG throughout the transport cycle ; a MalF periplasmic loop (MalF-P2) remains in close contact with MalE throughout the transport cycle ; MalF-P2 binds MalE in both the presence and absence of substrate . MalE is bound to MalFGK2 throughout the transport cycle; MalE binding correlates with structural rearrangement in MalF-P2 . Open-state (unliganded) MalE binds to reconstituted MalFGK2 and triggers cleavage of ATP; ATP cleavage is not stimulated by the closed (liganded) state of MalE; Pi release is the limiting factor in the ATPase cycle; maltose accelerates the release of Pi . Mutations that result in binding protein independent transport an

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.ABC-16-RXN|reaction.ecocyc.ABC-16-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7495|reaction.ecocyc.RXN0-7495]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-503|reaction.ecocyc.TRANS-RXN0-503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-504|reaction.ecocyc.TRANS-RXN0-504]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P02916|protein.P02916]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEX9|protein.P0AEX9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P68183|protein.P68183]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P68187|protein.P68187]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-16-CPLX`
- `PDB:3RLF`
- `PDB:3PV0`
- `PDB:3PUZ`
- `PDB:3PUY`
- `PDB:3PUX`
- `PDB:3PUW`
- `PDB:3PUV`
- `PDB:3FH6`
- `QSPROTEOME:QS00071274`

## Notes

2*protein.P68187|1*protein.P02916|1*protein.P68183|1*protein.P0AEX9
