---
entity_id: "complex.ecocyc.CPLX0-226"
entity_type: "complex"
name: "CRP-cyclic-AMP DNA-binding transcriptional dual regulator"
source_database: "EcoCyc"
source_id: "CPLX0-226"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "CRP-cAMP"
---

# CRP-cyclic-AMP DNA-binding transcriptional dual regulator

`complex.ecocyc.CPLX0-226`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-226`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.PC00004|complex.ecocyc.PC00004]], [[molecule.C00575|molecule.C00575]]

## Enriched Summary

The transcriptional dual regulator CRP, "cAMP receptor protein," also called CAP, "catabolite gene activator protein," regulates the expression of over 180 genes and indirectly regulates some translation in E. coli. Many of these genes are involved in the catabolism of secondary carbon sources (for reviews, see . In addition, CRP is involved in many other processes, such as osmoregulation , stringent response , biofilm formation , virulence , nitrogen assimilation , iron uptake , competence , multidrug resistance to antibiotics , PstI-CyaA-Crp-mediated cellular death process caused by stress , and expression of CyaR sRNA . Transcriptome analyses have been performed . Expression of crp is positively and negatively autoregulated ; repression of crp requires Fis . CRP plays an important role in persistent cell formation , as has been shown by activation of a gene potentially related to persistence . The activity of CRP on its targets indirectly reduces the expression of genes that are not CRP targets. This appears to happen because the regulation of CRP as a global regulator consumes the resources necessary for the expression of other genes, such as genes of anabolism . CRP also appears to be involved in the maintenance of cellular homeostasis through transcriptional regulation to respond to metabolic fluctuations under constant external cellular conditions...

## Annotation

The transcriptional dual regulator CRP, "cAMP receptor protein," also called CAP, "catabolite gene activator protein," regulates the expression of over 180 genes and indirectly regulates some translation in E. coli. Many of these genes are involved in the catabolism of secondary carbon sources (for reviews, see . In addition, CRP is involved in many other processes, such as osmoregulation , stringent response , biofilm formation , virulence , nitrogen assimilation , iron uptake , competence , multidrug resistance to antibiotics , PstI-CyaA-Crp-mediated cellular death process caused by stress , and expression of CyaR sRNA . Transcriptome analyses have been performed . Expression of crp is positively and negatively autoregulated ; repression of crp requires Fis . CRP plays an important role in persistent cell formation , as has been shown by activation of a gene potentially related to persistence . The activity of CRP on its targets indirectly reduces the expression of genes that are not CRP targets. This appears to happen because the regulation of CRP as a global regulator consumes the resources necessary for the expression of other genes, such as genes of anabolism . CRP also appears to be involved in the maintenance of cellular homeostasis through transcriptional regulation to respond to metabolic fluctuations under constant external cellular conditions . CRP was the first purified transcriptional regulator and the first regulator for which the structure was solved . CRP is activated as a DNA-binding protein via binding of its allosteric effector, cAMP . The hydrogen-bonding abilities of the Thr127 and Ser128 residues at the cAMP pocket play a key role in stabilizing the CRP inactive form and in providing high cAMP affinity. However, these residues are not critical for

## Outgoing Edges (10)

- `activates` --> [[gene.b0530|gene.b0530]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0719|gene.b0719]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0938|gene.b0938]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2339|gene.b2339]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3142|gene.b3142]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4055|gene.b4055]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4208|gene.b4208]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0473|gene.b0473]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0586|gene.b0586]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4006|gene.b4006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (2)

- `is_component_of` <-- [[complex.ecocyc.PC00004|complex.ecocyc.PC00004]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[molecule.C00575|molecule.C00575]] `EcoCyc` `database` - EcoCyc component coefficient=

## External IDs

- `EcoCyc:CPLX0-226`

## Notes

complex.ecocyc.PC00004|molecule.C00575
