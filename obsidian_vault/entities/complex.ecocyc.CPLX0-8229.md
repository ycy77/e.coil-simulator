---
entity_id: "complex.ecocyc.CPLX0-8229"
entity_type: "complex"
name: "antitoxin/DNA-binding transcriptional repressor HigA"
source_database: "EcoCyc"
source_id: "CPLX0-8229"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "HigA"
  - "HigA antitoxin of the HigB-HigA toxin-antitoxin system and DNA-binding transcriptional repressor"
---

# antitoxin/DNA-binding transcriptional repressor HigA

`complex.ecocyc.CPLX0-8229`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8229`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P67701|protein.P67701]]

## Enriched Summary

HigA is the antitoxin of the ribosome-dependent mRNA interferase toxin HigB. Ectopic expression of higB causes inhibition of cell growth which is alleviated by co-expression of higA . A crystal structure of the HigBA complex has been solved, showing a HigB-(HigA)2-HigB arrangement . The α1 helix in the N-terminal domain of HigA is essential for dimerization of HigA . The HigA C-terminal domain with a helix-turn-helix (HTH) fold is essential for DNA binding and for repression of the higBA operon . Comparison to a crystal structure of HigA alone suggests that HigA undergoes large conformational changes in its central domain upon interaction with HigB, which brings the C-terminal DNA binding domains of the HigA subunits closer together . HigA has the highest affinity to a palindromic region overlapping with the core promoter -35 region . Key residues for DNA binding were identified by site-directed mutagenesis . HigA antitoxin specifically recognizes a 27 bp palindromic operator sequence containing two 5'-CGTTGC-3' recognition motifs upstream of the higBA operon . The α7 helix and loop L2 of HigA make specific contacts with the palindromic DNA sequence . The promoter upstream of higB appears to be autorepressed by HigA; Lon protease is required for activation of transcription...

## Biological Role

Component of HigB-HigA toxin/antitoxin complex and DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-8230).

## Annotation

HigA is the antitoxin of the ribosome-dependent mRNA interferase toxin HigB. Ectopic expression of higB causes inhibition of cell growth which is alleviated by co-expression of higA . A crystal structure of the HigBA complex has been solved, showing a HigB-(HigA)2-HigB arrangement . The α1 helix in the N-terminal domain of HigA is essential for dimerization of HigA . The HigA C-terminal domain with a helix-turn-helix (HTH) fold is essential for DNA binding and for repression of the higBA operon . Comparison to a crystal structure of HigA alone suggests that HigA undergoes large conformational changes in its central domain upon interaction with HigB, which brings the C-terminal DNA binding domains of the HigA subunits closer together . HigA has the highest affinity to a palindromic region overlapping with the core promoter -35 region . Key residues for DNA binding were identified by site-directed mutagenesis . HigA antitoxin specifically recognizes a 27 bp palindromic operator sequence containing two 5'-CGTTGC-3' recognition motifs upstream of the higBA operon . The α7 helix and loop L2 of HigA make specific contacts with the palindromic DNA sequence . The promoter upstream of higB appears to be autorepressed by HigA; Lon protease is required for activation of transcription. Transcription is induced by chloramphenicol treatment as well as amino acid starvation induced by serine hydroxamate . HigA was transcriptionally upregulated in iron excess over iron limitation at 63% dissolved oxygen as determined by RNA-seq . Inhibition of higA expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic phleomycin . Review:

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8230|complex.ecocyc.CPLX0-8230]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P67701|protein.P67701]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8229`
- `QSPROTEOME:QS00199575`

## Notes

2*protein.P67701
