---
entity_id: "complex.ecocyc.CPLX0-8578"
entity_type: "complex"
name: "DNA-binding transcriptional repressor DgoR"
source_database: "EcoCyc"
source_id: "CPLX0-8578"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional repressor DgoR

`complex.ecocyc.CPLX0-8578`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8578`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P31460|protein.P31460]]

## Enriched Summary

DgoR belongs to the FadR subfamily within the GntR family of transcriptional regulators, and its DNA-binding operator sequence is [5'-TTGTA(G/C)TACA(A/T)-3'] . The signature of GntR family regulators that also bind inverted repeats is [5'-(N)yGT(N)xAC(N)y-3'] . As with the the other members of the family, the oligomeric form of DgoR is a dimer . There are three IRs (inverted repeats) in the regulation regions of the dgo genes. DgoR binds the IR1 and IR2 sites in the cis-acting element for repressing the dgoRKADT operon, and IR1 is essential for DgoR activity. The D7, L34, T40, R42, R46, and S51 amino acid residues are important for DgoR to bind its cis-acting element. On the other hand, the IR3 site is not critical for the interaction of DgoR with its cis-acting element . The DgoR binding sites overlap with the promoter, repressing the transcription of the dgoRKADT operon by occluding the binding of RNA polymerase . Based on a bioinformatics study, DgoR exists together with its binding sites in 13 genomes of different bacterial species, with the majority of members belonging to the family Enterobacteriaceae . Production of the enzymes involved in D-galactonate degradation are induced by growth on galactonate . The inducer is most likely D-galactonate itself; thus, DgoR may bind D-galactonate...

## Biological Role

Component of DgoR-D-galactonate (complex.ecocyc.CPLX0-8287).

## Annotation

DgoR belongs to the FadR subfamily within the GntR family of transcriptional regulators, and its DNA-binding operator sequence is [5'-TTGTA(G/C)TACA(A/T)-3'] . The signature of GntR family regulators that also bind inverted repeats is [5'-(N)yGT(N)xAC(N)y-3'] . As with the the other members of the family, the oligomeric form of DgoR is a dimer . There are three IRs (inverted repeats) in the regulation regions of the dgo genes. DgoR binds the IR1 and IR2 sites in the cis-acting element for repressing the dgoRKADT operon, and IR1 is essential for DgoR activity. The D7, L34, T40, R42, R46, and S51 amino acid residues are important for DgoR to bind its cis-acting element. On the other hand, the IR3 site is not critical for the interaction of DgoR with its cis-acting element . The DgoR binding sites overlap with the promoter, repressing the transcription of the dgoRKADT operon by occluding the binding of RNA polymerase . Based on a bioinformatics study, DgoR exists together with its binding sites in 13 genomes of different bacterial species, with the majority of members belonging to the family Enterobacteriaceae . Production of the enzymes involved in D-galactonate degradation are induced by growth on galactonate . The inducer is most likely D-galactonate itself; thus, DgoR may bind D-galactonate . D-galactonate is a specific effector of DgoR; it induces a conformational change in DgoR to derepress the dgoRKADT operon . D-galactonate binds to a specific cavity in DgoR located in the C-terminal domain. The cavity contains amino acids (R102, E106, D146, H150, Q173, W181, T180, M188, F142, W181, T191, L192, H195, S221, and R224 ) that are involved in effector binding . Beyond their involvement in D-galactonate sensing, individual residues in DgoR have been assigned specific fun

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8287|complex.ecocyc.CPLX0-8287]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31460|protein.P31460]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8578`
- `QSPROTEOME:QS00197283`

## Notes

2*protein.P31460
