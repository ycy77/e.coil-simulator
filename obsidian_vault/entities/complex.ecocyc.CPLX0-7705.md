---
entity_id: "complex.ecocyc.CPLX0-7705"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator Fis"
source_database: "EcoCyc"
source_id: "CPLX0-7705"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional dual regulator Fis

`complex.ecocyc.CPLX0-7705`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7705`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A6R3|protein.P0A6R3]]

## Enriched Summary

Fis, "factor for inversion stimulation", is a small DNA-binding and bending protein whose main role appears to be the organization and maintenance of nucleoid structure through direct DNA binding and by modulating gyrase and topoisomerase I production , as well as regulation of other proteins that modulate the nucleoid structure, such as CRP, H-NS, and HU. Fis does not play an architectural role in the H-NS-dependent three-dimensional organization of the nucleoid but may act as a potential anti-silencing factor at specific loci by competing with H-NS for DNA binding . Fis directly modulates several cellular processes, such as transcription, chromosomal replication, DNA inversion, phage integration/excision, and DNA transposition . Fis is able to form topological barriers blocking supercoiling diffusion around some promoters . To regulate DNA replication, Fis binds to six sites in a region, named DARS2, that promotes exchange of ADP/ATP in DnaA protein; DARS2 also contains five sites for DnaA and two sites for IHF . During preinitiation of replication, the site V for DnaA, which overlaps with the sites 4-5 of Fis, is occupied by ADP-DnaA, Fis is bound to the sites 2-3, and IHF is bound to the sites 1-2; this complex of proteins causes nucleotide exchange producing ATP-DnaA...

## Annotation

Fis, "factor for inversion stimulation", is a small DNA-binding and bending protein whose main role appears to be the organization and maintenance of nucleoid structure through direct DNA binding and by modulating gyrase and topoisomerase I production , as well as regulation of other proteins that modulate the nucleoid structure, such as CRP, H-NS, and HU. Fis does not play an architectural role in the H-NS-dependent three-dimensional organization of the nucleoid but may act as a potential anti-silencing factor at specific loci by competing with H-NS for DNA binding . Fis directly modulates several cellular processes, such as transcription, chromosomal replication, DNA inversion, phage integration/excision, and DNA transposition . Fis is able to form topological barriers blocking supercoiling diffusion around some promoters . To regulate DNA replication, Fis binds to six sites in a region, named DARS2, that promotes exchange of ADP/ATP in DnaA protein; DARS2 also contains five sites for DnaA and two sites for IHF . During preinitiation of replication, the site V for DnaA, which overlaps with the sites 4-5 of Fis, is occupied by ADP-DnaA, Fis is bound to the sites 2-3, and IHF is bound to the sites 1-2; this complex of proteins causes nucleotide exchange producing ATP-DnaA . When the levels of ATP-DnaA are high, the replication starts and ATP-DnaA oligomerizes, assisted by the protein DiaA, covering the 2-5 Fis sites and displacing to Fis; at the same time, IHF is also dissociated . Recent findings have further shown that Fis contributes to DARS2 activation by directly interacting with ADP-bound DnaA oligomers at the core DnaA boxes, in a mechanism that depends on DNA supercoiling and IHF-mediated DNA looping . The Gln68 residue of Fis is essential for this activation, a

## Outgoing Edges (2)

- `activates` --> [[gene.b1953|gene.b1953]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0740|gene.b0740]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6R3|protein.P0A6R3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7705`
- `QSPROTEOME:QS00196445`

## Notes

2*protein.P0A6R3
