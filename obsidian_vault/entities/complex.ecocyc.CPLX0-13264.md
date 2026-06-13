---
entity_id: "complex.ecocyc.CPLX0-13264"
entity_type: "complex"
name: "NrdR transcriptional Repressor"
source_database: "EcoCyc"
source_id: "CPLX0-13264"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NrdR transcriptional Repressor

`complex.ecocyc.CPLX0-13264`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13264`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8D0|protein.P0A8D0]]

## Enriched Summary

NrdR is a zinc-finger/ATP cone transcriptional regulatory protein that regulates the expression of several operons that encode ribonucleotide reductases (RNRs), according to the abundance of deoxyribonucleoside triphosphates (dNTPs) generated from ribonucleotides . NrdR has an N-terminal zinc-finger-like DNA-binding domain and a C-terminal ATP cone domain. The ATP cone domain is similar to the allosteric domain found in some RNRs . The Zn-ribbon domain interacts directly with DNA, and its relative orientation related to the ATP-cone domain changes drastically depending on the nucleotide-bound state. . As proposed by McKethan and Spiro , NrdR activity is modulated by nucleotide binding. They proposed a model in which NrdR binds (deoxy)nucleoside triphosphates, which are then hydrolyzed to monophosphates to regulate DNA binding. However, recent experimental evidence indicates that DNA binding by NrdR is promoted specifically by simultaneous binding to zinc, dATP, and ATP or ADP, while AMP and other monophosphates do not support DNA binding activity . These nucleotide combinations promote a flexible tetrameric conformation compatible with DNA binding . In contrast, when NrdR is bound to ATP alone, it forms helical filaments in which the residues responsible for DNA binding are sequestered within the interfaces between tetramers, thereby preventing DNA interaction...

## Biological Role

Component of NrdR-Zn2+ATP-dATP DNA transcriptional repressor (complex.ecocyc.CPLX0-8061).

## Annotation

NrdR is a zinc-finger/ATP cone transcriptional regulatory protein that regulates the expression of several operons that encode ribonucleotide reductases (RNRs), according to the abundance of deoxyribonucleoside triphosphates (dNTPs) generated from ribonucleotides . NrdR has an N-terminal zinc-finger-like DNA-binding domain and a C-terminal ATP cone domain. The ATP cone domain is similar to the allosteric domain found in some RNRs . The Zn-ribbon domain interacts directly with DNA, and its relative orientation related to the ATP-cone domain changes drastically depending on the nucleotide-bound state. . As proposed by McKethan and Spiro , NrdR activity is modulated by nucleotide binding. They proposed a model in which NrdR binds (deoxy)nucleoside triphosphates, which are then hydrolyzed to monophosphates to regulate DNA binding. However, recent experimental evidence indicates that DNA binding by NrdR is promoted specifically by simultaneous binding to zinc, dATP, and ATP or ADP, while AMP and other monophosphates do not support DNA binding activity . These nucleotide combinations promote a flexible tetrameric conformation compatible with DNA binding . In contrast, when NrdR is bound to ATP alone, it forms helical filaments in which the residues responsible for DNA binding are sequestered within the interfaces between tetramers, thereby preventing DNA interaction . In Streptomyces coelicolor, it was also shown that NrdR is an oligomeric protein that binds zinc, ATP, dATP . In other bacteria, NrdR acts as a negative regulator of nrd genes in Mycobacterium spp., Chlamydia trachomatis, and Salmonella enterica serovar Typhimurium ( and references therein). High-affinity DNA binding by NrdR requires the presence of two NrdR boxes, 16 bp palindromic motifs, separated by a spacer

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8061|complex.ecocyc.CPLX0-8061]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8D0|protein.P0A8D0]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-13264`

## Notes

4*protein.P0A8D0
