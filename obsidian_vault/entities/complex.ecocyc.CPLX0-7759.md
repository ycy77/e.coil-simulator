---
entity_id: "complex.ecocyc.CPLX0-7759"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator MetR"
source_database: "EcoCyc"
source_id: "CPLX0-7759"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional dual regulator MetR

`complex.ecocyc.CPLX0-7759`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7759`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9F9|protein.P0A9F9]]

## Enriched Summary

MetR participates in controlling several genes involved in methionine biosynthesis and a gene involved in protection against nitric oxide . Homocysteine, an intermediate in the biosynthesis of methionine , binds to MetR and enhances the activity of some MetR-activated promoters (i.e., metE and glyA) by enhancing the affinity in DNA-binding sites . But homocysteine is also able to decrease the activity of other promoters that are activated (i.e., metH, metA, and hmp) or repressed (i.e., metR) by MetR . The glyA and hmp genes are transcribed divergently and have a common regulatory region that contains two MetR DNA-binding sites. When homocysteine is present, MetR binds to two MetR sites and activates glyA and represses hmp transcription, but in the absence of homocysteine MetR binds only one site and activates hmp and represses glyA transcription . MetR appears to first bind DNA and then homocysteine causes the effect on transcription . The nitrosated compound S-nitrosoglutathione (GSNO) removes homocysteine by nitrosation . The RNA polymerase and MetR interact for transcription activation, but distinct residues of RNA polymerase are involved in different promoters because the MetR-binding sites are located at different positions |. MetR, as a dimer , recognizes and binds a DNA sequence with dyad symmetry...

## Biological Role

Component of MetR-L-homocysteine (complex.ecocyc.CPLX0-7752).

## Annotation

MetR participates in controlling several genes involved in methionine biosynthesis and a gene involved in protection against nitric oxide . Homocysteine, an intermediate in the biosynthesis of methionine , binds to MetR and enhances the activity of some MetR-activated promoters (i.e., metE and glyA) by enhancing the affinity in DNA-binding sites . But homocysteine is also able to decrease the activity of other promoters that are activated (i.e., metH, metA, and hmp) or repressed (i.e., metR) by MetR . The glyA and hmp genes are transcribed divergently and have a common regulatory region that contains two MetR DNA-binding sites. When homocysteine is present, MetR binds to two MetR sites and activates glyA and represses hmp transcription, but in the absence of homocysteine MetR binds only one site and activates hmp and represses glyA transcription . MetR appears to first bind DNA and then homocysteine causes the effect on transcription . The nitrosated compound S-nitrosoglutathione (GSNO) removes homocysteine by nitrosation . The RNA polymerase and MetR interact for transcription activation, but distinct residues of RNA polymerase are involved in different promoters because the MetR-binding sites are located at different positions |. MetR, as a dimer , recognizes and binds a DNA sequence with dyad symmetry . By using synthetic gene circuits, it was demonstrated that MetR activates transcription without evidence of stabilization of RNA polymerase (RNAP) . In the context of recent in vivo models proposing that many transcription factors primarily stabilize RNAP and that fold-changes scale inversely with promoter basal activity, MetR appears to be context-dependent, as synthetic gene circuits detected activation without evidence of RNAP stabilization . MetR belongs to the Ly

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7752|complex.ecocyc.CPLX0-7752]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9F9|protein.P0A9F9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7759`
- `QSPROTEOME:QS00049660`

## Notes

2*protein.P0A9F9
