---
entity_id: "complex.ecocyc.CPLX0-8109"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator/c-di-GMP phosphodiesterase PdeL"
source_database: "EcoCyc"
source_id: "CPLX0-8109"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PdeL"
---

# DNA-binding transcriptional dual regulator/c-di-GMP phosphodiesterase PdeL

`complex.ecocyc.CPLX0-8109`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8109`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21514|protein.P21514]]

## Enriched Summary

PdeL is an EC-3.1.4.52, consisting of an N-terminal LuxR-like DNA-binding domain and a C-terminal EAL domain that is required for phosphodiesterase activity . The isolated EAL domain of the enzyme is in a fast monomer-dimer equilibrium. Only the dimeric form of PdeL has phosphodiesterase activity, and substrate binding increases dimerization affinity . Crystal structures of the EAL domain alone and in various complexes have been solved, showing structural coupling between the dimer interface and the catalytic site . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeL. This supports a model whereby the signaling specificity of PDEs is the result of environmental signals required for their activation. Suppressor mutations in pdeL consisted of point mutations that are located within its catalytic EAL domain and resulted in higher levels of PdeL protein, increased enzymatic activity, reduced levels of intracellular c-di-GMP, and increased swimming motility . PdeL can be considered a molecule with enzymatic and regulatory capabilities due to its phosphodiesterase activity and its capability to bind to its own promoter region and stimulate its expression in response to c-di-GMP...

## Biological Role

Catalyzes RXN0-4181 (reaction.ecocyc.RXN0-4181). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

PdeL is an EC-3.1.4.52, consisting of an N-terminal LuxR-like DNA-binding domain and a C-terminal EAL domain that is required for phosphodiesterase activity . The isolated EAL domain of the enzyme is in a fast monomer-dimer equilibrium. Only the dimeric form of PdeL has phosphodiesterase activity, and substrate binding increases dimerization affinity . Crystal structures of the EAL domain alone and in various complexes have been solved, showing structural coupling between the dimer interface and the catalytic site . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeL. This supports a model whereby the signaling specificity of PDEs is the result of environmental signals required for their activation. Suppressor mutations in pdeL consisted of point mutations that are located within its catalytic EAL domain and resulted in higher levels of PdeL protein, increased enzymatic activity, reduced levels of intracellular c-di-GMP, and increased swimming motility . PdeL can be considered a molecule with enzymatic and regulatory capabilities due to its phosphodiesterase activity and its capability to bind to its own promoter region and stimulate its expression in response to c-di-GMP . PdeL is involved in the transcriptional regulation of genes related to motility and bacteriophage N4 resistance , and it is autoregulated . Based on ChIP-Seq analysis, it was observed that PdeL binds in the intergenic region of 10 genes . The pdeL gene is expressed at low levels . Like other transcription factors that bind DNA, the induction of high levels of PdeL causes nucleoid compaction and modifies the localization of proteins involved in replication and cell division

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `represses` --> [[gene.b3784|gene.b3784]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21514|protein.P21514]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8109`
- `QSPROTEOME:QS00196975`

## Notes

2*protein.P21514
