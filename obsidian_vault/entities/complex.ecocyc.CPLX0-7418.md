---
entity_id: "complex.ecocyc.CPLX0-7418"
entity_type: "complex"
name: "DNA-binding transcriptional repressor MprA"
source_database: "EcoCyc"
source_id: "CPLX0-7418"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional repressor MprA

`complex.ecocyc.CPLX0-7418`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7418`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ACR9|protein.P0ACR9]]

## Enriched Summary

The "E. coli multidrug resistance regulator" , EmrR, also known as MprA, "microcin production regulation, locus A" , negatively regulates the transcription of genes that code for multidrug resistance pumps that extrude structurally unrelated antimicrobial agents from the cell and possibly it also represses a gene that codes for a porin . Inhibition of mprA expression by CRISPRi enhanced cellular fitness under treatment with the antibiotics pyocyanin, rifampicin, verapamil or erythromycin, but reduced it under treatment with carbonyl cyanide 3-chlorophenylhydrazone (CCCP) or polymyxin B . When EmrR is overexpressed (the emrR gene in multicopy), it is able to repress the marRAB operon, which encodes two transcriptional regulators . EmrR has also been shown to be a repressor of plasmid-encoded genes involved in microcin biosynthesis . Microcins are low-molecular-weight polypeptide antibiotics . The MprA dimer binds 2,4-dinitrophenol, carbonyl cyanide m-chlorophenylhydrazone (CCCP), and carbonyl cyanide p-(trifluoro-methoxy)phenylhydrazone, predicted ligands of the EmrAB pump, with high affinity . MprA also is able to bind to salicylate and to a small drug-like molecule inhibitor of capsule biogenesis named DUO11 . Binding of any of these agents interferes with the ability of MprA to bind DNA . This dimeric protein recognizes and binds an imperfect inverted repeat DNA sequence...

## Biological Role

Component of MprA-2,4-dinitrophenol (complex.ecocyc.CPLX0-7742), MprA-carbonylcyanide m-chlorophenylhydrazone (complex.ecocyc.CPLX0-7743), MprA-salicylate (complex.ecocyc.CPLX0-8579).

## Annotation

The "E. coli multidrug resistance regulator" , EmrR, also known as MprA, "microcin production regulation, locus A" , negatively regulates the transcription of genes that code for multidrug resistance pumps that extrude structurally unrelated antimicrobial agents from the cell and possibly it also represses a gene that codes for a porin . Inhibition of mprA expression by CRISPRi enhanced cellular fitness under treatment with the antibiotics pyocyanin, rifampicin, verapamil or erythromycin, but reduced it under treatment with carbonyl cyanide 3-chlorophenylhydrazone (CCCP) or polymyxin B . When EmrR is overexpressed (the emrR gene in multicopy), it is able to repress the marRAB operon, which encodes two transcriptional regulators . EmrR has also been shown to be a repressor of plasmid-encoded genes involved in microcin biosynthesis . Microcins are low-molecular-weight polypeptide antibiotics . The MprA dimer binds 2,4-dinitrophenol, carbonyl cyanide m-chlorophenylhydrazone (CCCP), and carbonyl cyanide p-(trifluoro-methoxy)phenylhydrazone, predicted ligands of the EmrAB pump, with high affinity . MprA also is able to bind to salicylate and to a small drug-like molecule inhibitor of capsule biogenesis named DUO11 . Binding of any of these agents interferes with the ability of MprA to bind DNA . This dimeric protein recognizes and binds an imperfect inverted repeat DNA sequence . MprA belongs to the MarR family of transcriptional regulators , which respond to a variety of phenolic compounds and are found in gram-positive and gram-negative species as well as in mycobacteria . The proteins of this family have a helix-turn-helix DNA-binding motif at the center , while the ligand-binding domain is possibly located at the N-terminal domain . MprA shows 28% and 47% identity and si

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7742|complex.ecocyc.CPLX0-7742]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7743|complex.ecocyc.CPLX0-7743]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8579|complex.ecocyc.CPLX0-8579]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACR9|protein.P0ACR9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7418`
- `QSPROTEOME:QS00049621`

## Notes

2*protein.P0ACR9
