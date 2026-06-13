---
entity_id: "complex.ecocyc.PC00061"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator Cra"
source_database: "EcoCyc"
source_id: "PC00061"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FruR"
  - "Cra"
---

# DNA-binding transcriptional dual regulator Cra

`complex.ecocyc.PC00061`

## Static

- Type: `complex`
- Source: `EcoCyc:PC00061`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ACP1|protein.P0ACP1]]

## Enriched Summary

"Catabolite repressor activator," Cra, which was initially named "Fructose repressor," "FruR," is a dual transcriptional regulator that plays a pleiotropic role to modulate the direction of carbon flow through the different metabolic pathways of energy metabolism, but independently of the CRP regulator . For this reason the Cra regulator is implicated in the expression of a large number of operons that encode enzymes which comprise central pathways of carbon metabolism . Cra acts as an activator of genes encoding gluconeogenic , Krebs cycle , and glyoxylate shunt enzymes, and the negative effect on genes encoding Entner-Doudoroff pathway and glycolytic enzymes . Inhibition of cra expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic novobiocin, but reduced it under treatment with carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . Cra carries out a glycolytic flux-dependent regulation. The glycolytic flux is determined by the concentration of the metabolite fructose-1,6-bisphosphate (FBP), which is a molecule that was previously thought to be a molecular effector of Cra , but it has recently been shown that FBP neither binds nor regulates Cra DNA-binding activity . Cra forms a complex with DNA in the absence of fructose 1-phosphate, binding to an 18-bp-long sequence with an imperfect palindromic sequence...

## Biological Role

Component of Cra-β-D-fructofuranose 1-phosphate (complex.ecocyc.CPLX-127).

## Annotation

"Catabolite repressor activator," Cra, which was initially named "Fructose repressor," "FruR," is a dual transcriptional regulator that plays a pleiotropic role to modulate the direction of carbon flow through the different metabolic pathways of energy metabolism, but independently of the CRP regulator . For this reason the Cra regulator is implicated in the expression of a large number of operons that encode enzymes which comprise central pathways of carbon metabolism . Cra acts as an activator of genes encoding gluconeogenic , Krebs cycle , and glyoxylate shunt enzymes, and the negative effect on genes encoding Entner-Doudoroff pathway and glycolytic enzymes . Inhibition of cra expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic novobiocin, but reduced it under treatment with carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . Cra carries out a glycolytic flux-dependent regulation. The glycolytic flux is determined by the concentration of the metabolite fructose-1,6-bisphosphate (FBP), which is a molecule that was previously thought to be a molecular effector of Cra , but it has recently been shown that FBP neither binds nor regulates Cra DNA-binding activity . Cra forms a complex with DNA in the absence of fructose 1-phosphate, binding to an 18-bp-long sequence with an imperfect palindromic sequence . In the presence of glucose it increases the intracellular concentration of the metabolites D-fructose 1-phosphate, which interact with Cra to prevent its binding or displacement of the target operons . Cra is inactivated upon the interaction of the inducers. Cra has been observed to be predominantly a tetrameric structure in solution . The complex formation of Cra with the enzyme fructose-1-kinase (1-PFK FruK) has been demonstrated . This e

## Outgoing Edges (10)

- `activates` --> [[gene.b1703|gene.b1703]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1777|gene.b1777]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2007|gene.b2007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2074|gene.b2074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2597|gene.b2597]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3829|gene.b3829]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4232|gene.b4232]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `is_component_of` --> [[complex.ecocyc.CPLX-127|complex.ecocyc.CPLX-127]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1242|gene.b1242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1675|gene.b1675]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACP1|protein.P0ACP1]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PC00061`
- `QSPROTEOME:QS00181907`

## Notes

4*protein.P0ACP1
