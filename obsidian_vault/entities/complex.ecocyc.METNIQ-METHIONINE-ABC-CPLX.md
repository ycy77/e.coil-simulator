---
entity_id: "complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX"
entity_type: "complex"
name: "L-methionine/D-methionine ABC transporter"
source_database: "EcoCyc"
source_id: "METNIQ-METHIONINE-ABC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-methionine/D-methionine ABC transporter

`complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:METNIQ-METHIONINE-ABC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P30750|protein.P30750]], [[protein.P31547|protein.P31547]], [[protein.P28635|protein.P28635]]

## Enriched Summary

MetNIQ is a high affinity methionine uptake system that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Early studies characterized the metD locus which was responsible for the high affinity transport of both isomers of methionine and also for the uptake of N-acetyl methionine and methionine sulfoxide . Methionine transport in E. coli K-12 is subject to transinhibition - it is modulated by the level of the intracellular methionine pool . Deletion of each of the single loci metN, metI and metQ in a methionine auxotroph (metE3079::Tn10) results in strains that have impaired growth with D-methionine as sole methionine source . Deletion of all three genes in a methionine auxotroph (ΔmetE ΔMetH) results in a strain that is unable to grow with D-methionine as sole methionine source; complementation of this phenotype requires extrachromosomal expression of all three genes . A strain lacking the metNIQ gene cluster is also resistant to the toxic methionine analogue, α-methyl methionine . The MetNIQ transporter is specific for both methionine isomers and can transport N-formyl methionine . Sequence analysis suggests that MetN is the ATP binding subunit, MetI the integral membrane component and MetQ a membrane anchored, substrate binding protein, of the transporter complex...

## Biological Role

Catalyzes RXN0-4522 (reaction.ecocyc.RXN0-4522), TRANS-RXN-383 (reaction.ecocyc.TRANS-RXN-383), TRANS-RXN0-202 (reaction.ecocyc.TRANS-RXN0-202), TRANS-RXN0-510 (reaction.ecocyc.TRANS-RXN0-510), TRANS-RXN0-511 (reaction.ecocyc.TRANS-RXN0-511). Transports L-Methionine (molecule.C00073), D-Methionine (molecule.C00855), L-Methionine S-oxide (molecule.C02989), D-selenomethionine (molecule.ecocyc.CPD-21777), N-acetyl-DL-methionine (molecule.ecocyc.CPD-3738), hν (molecule.ecocyc.Light).

## Annotation

MetNIQ is a high affinity methionine uptake system that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Early studies characterized the metD locus which was responsible for the high affinity transport of both isomers of methionine and also for the uptake of N-acetyl methionine and methionine sulfoxide . Methionine transport in E. coli K-12 is subject to transinhibition - it is modulated by the level of the intracellular methionine pool . Deletion of each of the single loci metN, metI and metQ in a methionine auxotroph (metE3079::Tn10) results in strains that have impaired growth with D-methionine as sole methionine source . Deletion of all three genes in a methionine auxotroph (ΔmetE ΔMetH) results in a strain that is unable to grow with D-methionine as sole methionine source; complementation of this phenotype requires extrachromosomal expression of all three genes . A strain lacking the metNIQ gene cluster is also resistant to the toxic methionine analogue, α-methyl methionine . The MetNIQ transporter is specific for both methionine isomers and can transport N-formyl methionine . Sequence analysis suggests that MetN is the ATP binding subunit, MetI the integral membrane component and MetQ a membrane anchored, substrate binding protein, of the transporter complex . Crystal structures of MetNI in an inward facing, ATPase inactive conformation have been reported; the structures contain two copies of MetN in complex with two copies of MetI; binding of methionine to a dimerized MetN C-terminal extension (the C2 domain) stabilizes the ATPase inactive conformation; L-methionine and L-selenomethionine, but not D-methionine, inhibit the ATPase activity of detergent solubilized MetNI . L-methionine is a non-competitive inhibitor of MetNI ATPase activit

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4522|reaction.ecocyc.RXN0-4522]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-383|reaction.ecocyc.TRANS-RXN-383]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-202|reaction.ecocyc.TRANS-RXN0-202]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-510|reaction.ecocyc.TRANS-RXN0-510]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-511|reaction.ecocyc.TRANS-RXN0-511]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00855|molecule.C00855]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C02989|molecule.C02989]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-21777|molecule.ecocyc.CPD-21777]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-3738|molecule.ecocyc.CPD-3738]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P28635|protein.P28635]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P30750|protein.P30750]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P31547|protein.P31547]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:METNIQ-METHIONINE-ABC-CPLX`
- `PDB:3DHW`
- `PDB:3TUI`
- `PDB:3TUJ`
- `PDB:3TUZ`
- `PDB:6CVL`
- `PDB:6CVL`
- `QSPROTEOME:QS00220416`

## Notes

2*protein.P30750|2*protein.P31547|1*protein.P28635
