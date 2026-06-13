---
entity_id: "complex.ecocyc.CPLX0-7666"
entity_type: "complex"
name: "DNA-binding transcriptional activator CaiF"
source_database: "EcoCyc"
source_id: "CPLX0-7666"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional activator CaiF

`complex.ecocyc.CPLX0-7666`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7666`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AE58|protein.P0AE58]]

## Enriched Summary

Under anaerobiosis and in the presence of "carnitine," CaiF activates the transcription of genes involved in carnitine metabolism . This protein recognizes and binds to two 11-bp inverted repeat half-sites separated by 13 bp in the intergenic region of two operons located divergently in the genome (caiTABCDE and fixABCX). CaiF possibly binds as a dimer, with each monomer of the complex recognizing one half of the site. A genome-wide computerized scan demonstrated that there are no more sites in the genome for CaiF . A complex composed of two CRP dimers and two CaiF dimers needs to be bound in order for the RNA polymerase to bind to the promoter. CRP, which makes contact with the RNA polymerase, seems to be the main protein of the complex. CaiF was suggested to counteract the repression effect of HNS. It has been proposed that CRP and CaiF bind to opposite DNA strands . Carnitine and crotonobetaine, the putative inducers of carnitine metabolism, seem to be of no help in CaiF binding . The DNA-binding motif of CaiF, which does not have a typical helix-turn-helix arrangement , is located in the C-terminal domain, whereas the N-terminal domain contains a structural organization motif that could be useful in formation of dimers...

## Biological Role

Component of CaiF-L-carnitine DNA-binding Transcriptional Activator (complex.ecocyc.CPLX0-8062).

## Annotation

Under anaerobiosis and in the presence of "carnitine," CaiF activates the transcription of genes involved in carnitine metabolism . This protein recognizes and binds to two 11-bp inverted repeat half-sites separated by 13 bp in the intergenic region of two operons located divergently in the genome (caiTABCDE and fixABCX). CaiF possibly binds as a dimer, with each monomer of the complex recognizing one half of the site. A genome-wide computerized scan demonstrated that there are no more sites in the genome for CaiF . A complex composed of two CRP dimers and two CaiF dimers needs to be bound in order for the RNA polymerase to bind to the promoter. CRP, which makes contact with the RNA polymerase, seems to be the main protein of the complex. CaiF was suggested to counteract the repression effect of HNS. It has been proposed that CRP and CaiF bind to opposite DNA strands . Carnitine and crotonobetaine, the putative inducers of carnitine metabolism, seem to be of no help in CaiF binding . The DNA-binding motif of CaiF, which does not have a typical helix-turn-helix arrangement , is located in the C-terminal domain, whereas the N-terminal domain contains a structural organization motif that could be useful in formation of dimers . By using synthetic gene circuits, it was suggested that CaiF changes the strength of its repression effect depending on the position of the binding site relative to the promoter . The caiF gene, which is located downstream and in the opposite direction to one of the operons (cai) that it regulates, is induced under anaerobic conditions .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8062|complex.ecocyc.CPLX0-8062]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AE58|protein.P0AE58]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7666`
- `QSPROTEOME:QS00049434`

## Notes

2*protein.P0AE58
