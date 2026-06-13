---
entity_id: "complex.ecocyc.CPLX0-7796"
entity_type: "complex"
name: "DNA-binding transcriptional repressor MetJ-S-adenosyl-L-methionine"
source_database: "EcoCyc"
source_id: "CPLX0-7796"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MetJ-S-adenosylmethionine"
---

# DNA-binding transcriptional repressor MetJ-S-adenosyl-L-methionine

`complex.ecocyc.CPLX0-7796`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7796`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.MONOMER0-157|complex.ecocyc.MONOMER0-157]]

## Enriched Summary

MetJ represses the expression of genes involved in biosynthesis and transport of methionine . MetJ belongs to the ribbon-helix-helix family of regulatory proteins. The typical motif of members of this family, the ribbon-helix-helix motif for DNA binding, has been observed in the crystalline structure of MetJ . This motif is composed of a two-stranded antiparallel β-ribbon that lies along the DNA major groove, two outer α-helices that interact with adjacent proteins along the DNA, and two inner β-helices that form the subunit interface . MetJ as a homodimer recognizes and binds to an 8-bp DNA sequence called the met-box, which varies around a perfect palindromic consensus sequence . MetJ finds its target sites rapidly by facilitated diffusion . The affinity of MetJ to this site is enhanced by S-adenosyl methionine (AdoMet) , which is the end product of methionine biosynthesis and which binds MetJ to act as a corepressor . The binding of AdoMet to MetJ creates an unusually long-range electrostatic interaction with the phosphodiester backbone of the DNA, raising the DNA affinity by at least 100-fold . In addition to AdoMet, the metabolites 5'-deoxy-5'-(methylthio)adenosine (MTA) and adenine (Ade) also bind with high affinity to MetJ, but the biological effects of this binding are not known...

## Biological Role

Component of MetJ-SAM-AdoMet (complex.ecocyc.CPLX0-11744).

## Annotation

MetJ represses the expression of genes involved in biosynthesis and transport of methionine . MetJ belongs to the ribbon-helix-helix family of regulatory proteins. The typical motif of members of this family, the ribbon-helix-helix motif for DNA binding, has been observed in the crystalline structure of MetJ . This motif is composed of a two-stranded antiparallel β-ribbon that lies along the DNA major groove, two outer α-helices that interact with adjacent proteins along the DNA, and two inner β-helices that form the subunit interface . MetJ as a homodimer recognizes and binds to an 8-bp DNA sequence called the met-box, which varies around a perfect palindromic consensus sequence . MetJ finds its target sites rapidly by facilitated diffusion . The affinity of MetJ to this site is enhanced by S-adenosyl methionine (AdoMet) , which is the end product of methionine biosynthesis and which binds MetJ to act as a corepressor . The binding of AdoMet to MetJ creates an unusually long-range electrostatic interaction with the phosphodiester backbone of the DNA, raising the DNA affinity by at least 100-fold . In addition to AdoMet, the metabolites 5'-deoxy-5'-(methylthio)adenosine (MTA) and adenine (Ade) also bind with high affinity to MetJ, but the biological effects of this binding are not known . The genes regulated by MetJ contain in their regulatory region two to five continuous met-boxes , in which MetJ dimers interact with each other . A positive correlation between cellular growth and the copy number of the protein MetJ has been reported . The metJ gene, which is autoregulated, is transcribed divergently from the metBL operon, which is repressed by MetJ . Mutations in metJ have been observed in tolerant cells to two chemical diols, 1,2-propanediol, and 2,3-butanediol . Inh

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11744|complex.ecocyc.CPLX0-11744]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `is_component_of` <-- [[complex.ecocyc.MONOMER0-157|complex.ecocyc.MONOMER0-157]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0A8U6|protein.P0A8U6]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7796`
- `QSPROTEOME:QS00164275`

## Notes

2*complex.ecocyc.MONOMER0-157
