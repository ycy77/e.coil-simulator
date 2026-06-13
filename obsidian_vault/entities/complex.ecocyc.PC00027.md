---
entity_id: "complex.ecocyc.PC00027"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator IHF"
source_database: "EcoCyc"
source_id: "PC00027"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "IHF"
  - "integration host factor"
  - "DNA bending protein IHF"
---

# DNA-binding transcriptional dual regulator IHF

`complex.ecocyc.PC00027`

## Static

- Type: `complex`
- Source: `EcoCyc:PC00027`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A6X7|protein.P0A6X7]], [[protein.P0A6Y1|protein.P0A6Y1]]

## Enriched Summary

IHF, "Integration host factor," is a global regulatory protein that helps to maintain DNA architecture. It binds and bends DNA at specific sites. IHF plays a role in DNA supercoiling and DNA duplex destabilization and affects processes such as DNA replication, recombination, and the expression of many genes . To regulate DNA replication, IHF binds to three loci in DNA, named oriC (origin of replication), datA (prevents untimely replication initiations), and DARS2 (promotes exchange of ADP/ATP in DnaA protein) . Before DNA replication initiation, IHF binds to the oriC region in a DnaA box R1-dependent manner and to the DARS2 region, and it is rapidly released from these sites after replication initiation to bind to other loci |. There are two specific binding sites for IHF in the oriC region and two in the DARS2 region . At DARS2, IHF plays a central role by binding to the IBS1-2 site and inducing DNA bending that facilitates the dissociation of ADP from DnaA . Importantly, this function depends on negative DNA supercoiling, stabilizing IHF binding to DARS2 . IHF is dissociated from the datA sequence due to the read-through transcription of the glyVXY operon located upstream of datA in a cell cycle-dependent manner...

## Annotation

IHF, "Integration host factor," is a global regulatory protein that helps to maintain DNA architecture. It binds and bends DNA at specific sites. IHF plays a role in DNA supercoiling and DNA duplex destabilization and affects processes such as DNA replication, recombination, and the expression of many genes . To regulate DNA replication, IHF binds to three loci in DNA, named oriC (origin of replication), datA (prevents untimely replication initiations), and DARS2 (promotes exchange of ADP/ATP in DnaA protein) . Before DNA replication initiation, IHF binds to the oriC region in a DnaA box R1-dependent manner and to the DARS2 region, and it is rapidly released from these sites after replication initiation to bind to other loci |. There are two specific binding sites for IHF in the oriC region and two in the DARS2 region . At DARS2, IHF plays a central role by binding to the IBS1-2 site and inducing DNA bending that facilitates the dissociation of ADP from DnaA . Importantly, this function depends on negative DNA supercoiling, stabilizing IHF binding to DARS2 . IHF is dissociated from the datA sequence due to the read-through transcription of the glyVXY operon located upstream of datA in a cell cycle-dependent manner . The IHF protein binds with a strong affinity to the central region of the structures formed during DNA repair and homologous recombination, known as Holliday junctions, to stabilize the open conformation of these structures . IHF is highly abundant in the cell. Its total intracellular concentration varies with growth rate and is higher in exponential phase, with 6,000 dimers per cell, than in stationary phase (3,000 dimers per cell) . IHF acts mostly as an accessory factor, stabilizing a correct nucleoprotein complex. For example, IHF was originally found to

## Outgoing Edges (2)

- `activates` --> [[gene.b4208|gene.b4208]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1136|gene.b1136]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0A6X7|protein.P0A6X7]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A6Y1|protein.P0A6Y1]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:PC00027`
- `PDB:1OWG`
- `PDB:2IIF`
- `PDB:2IIE`
- `PDB:2HT0`
- `PDB:1OWF`
- `PDB:1OUZ`
- `PDB:1IHF`
- `PDB:5J0N`
- `QSPROTEOME:QS00177453`

## Notes

protein.P0A6X7|protein.P0A6Y1
