---
entity_id: "complex.ecocyc.CPLX0-7740"
entity_type: "complex"
name: "DNA-binding transcriptional repressor CytR"
source_database: "EcoCyc"
source_id: "CPLX0-7740"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional repressor CytR

`complex.ecocyc.CPLX0-7740`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7740`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ACN7|protein.P0ACN7]]

## Enriched Summary

CytR, "Cytidine Regulator," is a transcription factor required for transport and utilization of ribonucleosides and deoxyribonucleosides . Subsequently, a role for CytR in carbon catabolism was suggested . The repressor CytR and the activator CRP, two dimeric proteins, interact to form a complex repressor nucleoprotein in the intergenic region . Footprinting analyses showed that the dimers of CytR are flanked or "sandwiched" by two dimers of CRP . At times, CytR also repositions CRP to alternative DNA-binding sites that are not functional for activation . When only CRP is bound to this promoter, it functions as an activator, and then, when CytR binds to DNA and to CRP, the activation is repressed because CytR masks an activating region of CRP that otherwise would contact the RNA polymerase to activate transcription . Gavigan et al. (1999) and Perini et al. (1996) showed that CytR binds in tandem in the regulated intergenic region . On the other hand, in 1997, Pedersen and Valentin-Hanses showed that CytR binds to octamer repeats, GTTGCATT, in either the direct or inverted orientation and preferably separated by 2 or 3 bp . For this reason the length of the CytR DNA-binding site is variable. By using synthetic gene circuits, it was suggested that CytR does not change the strength of its repression effect at different positions of the binding site relative to the promoter...

## Biological Role

Component of CytR-cytidine (complex.ecocyc.CPLX0-8051).

## Annotation

CytR, "Cytidine Regulator," is a transcription factor required for transport and utilization of ribonucleosides and deoxyribonucleosides . Subsequently, a role for CytR in carbon catabolism was suggested . The repressor CytR and the activator CRP, two dimeric proteins, interact to form a complex repressor nucleoprotein in the intergenic region . Footprinting analyses showed that the dimers of CytR are flanked or "sandwiched" by two dimers of CRP . At times, CytR also repositions CRP to alternative DNA-binding sites that are not functional for activation . When only CRP is bound to this promoter, it functions as an activator, and then, when CytR binds to DNA and to CRP, the activation is repressed because CytR masks an activating region of CRP that otherwise would contact the RNA polymerase to activate transcription . Gavigan et al. (1999) and Perini et al. (1996) showed that CytR binds in tandem in the regulated intergenic region . On the other hand, in 1997, Pedersen and Valentin-Hanses showed that CytR binds to octamer repeats, GTTGCATT, in either the direct or inverted orientation and preferably separated by 2 or 3 bp . For this reason the length of the CytR DNA-binding site is variable. By using synthetic gene circuits, it was suggested that CytR does not change the strength of its repression effect at different positions of the binding site relative to the promoter . Gene induction occurs when the physiological inducer, cytidine, binds to the CytR regulator and when cellular cAMP levels are high. CytR senses and binds cytidine, and when this happens the cooperativity of CytR and CRP is interrupted and the expression of genes is induced . When CytR is unbound to DNA, its DNA-binding domains show two different states, one of them is unfolded (the most) and the other

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8051|complex.ecocyc.CPLX0-8051]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b4055|gene.b4055]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACN7|protein.P0ACN7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7740`
- `QSPROTEOME:QS00049652`

## Notes

2*protein.P0ACN7
