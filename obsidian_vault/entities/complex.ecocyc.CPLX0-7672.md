---
entity_id: "complex.ecocyc.CPLX0-7672"
entity_type: "complex"
name: "MntR-Mn2+ DNA-binding transcriptional dual regulator"
source_database: "EcoCyc"
source_id: "CPLX0-7672"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# MntR-Mn2+ DNA-binding transcriptional dual regulator

`complex.ecocyc.CPLX0-7672`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7672`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-7701|complex.ecocyc.CPLX0-7701]]

## Enriched Summary

MntR, "Mn2+ transport regulator", the primary sensor and transducer of manganese abundance, is a dual regulator that senses manganese and negatively or positively controls the transcription of different genes involved in manganese homeostasis . It has been demonstrated that MntR is necessary for the resumption of the replication process following hydrogen peroxide stress, through its role as a regulator of manganese homeostasis . This protein belongs to the DtxR family. The members of this family have three domains: an N-terminal domain with a helix-turn-helix motif, which binds to DNA; a central domain for dimerization and metal ion binding; and a C-terminal alpha-spectrin SH3-like domain. However, MntR lacks the SH3-like domain . The 3D structure of apo-MntR has been solved. The protein dimerizes via its C-terminal domain. The N-terminal and C-terminal domains are connected by a long α-helical linker . The N-terminal domain is expected to bind two manganese ions per monomer, in analogy to BsMntR from B. subtilis, which has been crystallized with and without bound manganese . All residues involved in manganese binding in BsMntR ar conserved in MntR . MntR does not seem to be autoregulated . Many iron acquisition genes are derepressed in the mntR mutant . In an mntR knockout mutant, cellular growth was reduced compared with the wild type...

## Biological Role

Component of MntR-Mn2+ (complex.ecocyc.CPLX0-10669).

## Annotation

MntR, "Mn2+ transport regulator", the primary sensor and transducer of manganese abundance, is a dual regulator that senses manganese and negatively or positively controls the transcription of different genes involved in manganese homeostasis . It has been demonstrated that MntR is necessary for the resumption of the replication process following hydrogen peroxide stress, through its role as a regulator of manganese homeostasis . This protein belongs to the DtxR family. The members of this family have three domains: an N-terminal domain with a helix-turn-helix motif, which binds to DNA; a central domain for dimerization and metal ion binding; and a C-terminal alpha-spectrin SH3-like domain. However, MntR lacks the SH3-like domain . The 3D structure of apo-MntR has been solved. The protein dimerizes via its C-terminal domain. The N-terminal and C-terminal domains are connected by a long α-helical linker . The N-terminal domain is expected to bind two manganese ions per monomer, in analogy to BsMntR from B. subtilis, which has been crystallized with and without bound manganese . All residues involved in manganese binding in BsMntR ar conserved in MntR . MntR does not seem to be autoregulated . Many iron acquisition genes are derepressed in the mntR mutant . In an mntR knockout mutant, cellular growth was reduced compared with the wild type .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10669|complex.ecocyc.CPLX0-10669]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7701|complex.ecocyc.CPLX0-7701]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0A9F1|protein.P0A9F1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7672`
- `QSPROTEOME:QS00183169`

## Notes

2*complex.ecocyc.CPLX0-7701
