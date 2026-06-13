---
entity_id: "protein.P23842"
entity_type: "protein"
name: "pdeA"
source_database: "UniProt"
source_id: "P23842"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeA yfeA b2395 JW5391"
---

# pdeA

`protein.P23842`

## Static

- Type: `protein`
- Source: `UniProt:P23842`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. PdeA is a predicted c-di-GMP phosphodiesterase that consists of an N-terminal MASE1 (Membrane-Associated SEnsor) domain followed by a degenerate GGDEF domain and a C-terminal EAL domain . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeA. This supports a model whereby the signaling specificity of PDEs is the result of environmental signals required for their activation. The suppressor mutation in pdeA consisted of a single amino acid substitution in the N-terminal membrane sensory domain of PdeA and resulted in increased swimming motility and reduced levels of intracellular c-di-GMP . pdeA is expressed during exponential growth in rich medium . PdeA: "phosphodiesterase A"

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52

## Incoming Edges (1)

- `encodes` <-- [[gene.b2395|gene.b2395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23842`
- `KEGG:ecj:JW5391;eco:b2395;ecoc:C3026_13310;`
- `GeneID:75202538;946864;`
- `GO:GO:0005886; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeA (EC 3.1.4.52)
