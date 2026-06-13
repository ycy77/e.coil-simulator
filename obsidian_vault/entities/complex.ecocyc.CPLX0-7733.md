---
entity_id: "complex.ecocyc.CPLX0-7733"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator AsnC"
source_database: "EcoCyc"
source_id: "CPLX0-7733"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional dual regulator AsnC

`complex.ecocyc.CPLX0-7733`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7733`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ACI6|protein.P0ACI6]]

## Enriched Summary

AsnC is a transcriptional regulator that activates the expression of asnA, a gene involved in the synthesis of asparagine . However, when asparagine is present the activation of asnA is turned off. On the other hand, AsnC is negatively autoregulated, but the presence of asparagine does not affect this regulation . AsnC belongs to the AsnC family of regulatory proteins whose members are widely distributed in archaea and bacteria . It has been postulated that AsnC is very ancient; it appears that it was present before the divergence of archaea and bacteria . This protein has a DNA-binding domain with a helix-turn-helix motif in the N terminus and an effector-binding C-terminal domain . A crystal structure of AsnC complexed with the ligand L-asparagine has been solved at 2.4-Å resolution. The crystal structure shows an octamer with l-asparagine bound in a cleft at the interface between dimers; however, the octamer is formed in an L-asparagine-independent manner . The octamer is composed of four dimers, each of which appears to recognize and bind an inverted repeat DNA sequence of 5 bp separated by 3 bp that are usually T or A base pairs. There are four AsnC sites in the divergent regulatory regions of asnA and asnC, and they are separated by 18 bp...

## Biological Role

Component of AsnC-L-asparagine (complex.ecocyc.CPLX0-7735).

## Annotation

AsnC is a transcriptional regulator that activates the expression of asnA, a gene involved in the synthesis of asparagine . However, when asparagine is present the activation of asnA is turned off. On the other hand, AsnC is negatively autoregulated, but the presence of asparagine does not affect this regulation . AsnC belongs to the AsnC family of regulatory proteins whose members are widely distributed in archaea and bacteria . It has been postulated that AsnC is very ancient; it appears that it was present before the divergence of archaea and bacteria . This protein has a DNA-binding domain with a helix-turn-helix motif in the N terminus and an effector-binding C-terminal domain . A crystal structure of AsnC complexed with the ligand L-asparagine has been solved at 2.4-Å resolution. The crystal structure shows an octamer with l-asparagine bound in a cleft at the interface between dimers; however, the octamer is formed in an L-asparagine-independent manner . The octamer is composed of four dimers, each of which appears to recognize and bind an inverted repeat DNA sequence of 5 bp separated by 3 bp that are usually T or A base pairs. There are four AsnC sites in the divergent regulatory regions of asnA and asnC, and they are separated by 18 bp . The replication origin, oriC, is located between the mioC and gidA genes, and the asnC gene is immediately upstream of mioC in the genome . The transcription of asnC sometimes traverses the origin of replication and continues into gidA, possibly explaining the effect on gidA expression . Sometimes the transcription of asnC ends at a terminator located downstream of this gene or by the DnaA protein that binds to a DnaA box blocking the transcribing RNA polymerase . Expression of asnC is regulated by nitrogen availability; under

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7735|complex.ecocyc.CPLX0-7735]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACI6|protein.P0ACI6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7733`
- `QSPROTEOME:QS00049650`

## Notes

2*protein.P0ACI6
