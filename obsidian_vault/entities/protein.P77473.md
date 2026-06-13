---
entity_id: "protein.P77473"
entity_type: "protein"
name: "pdeB"
source_database: "UniProt"
source_id: "P77473"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeB ylaB b0457 JW5062"
---

# pdeB

`protein.P77473`

## Static

- Type: `protein`
- Source: `UniProt:P77473`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. PdeB is a predicted c-di-GMP-specific phosphodiesterase whose activity is implicated in modulating matrix formation in E. coli biofilm. PdeB is an inner membrane protein with two predicted transmembrane domains which flank a predicted periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeB belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . PdeB, like EG11938-MONOMER "PdeC", is subject to redox control and and DegP/DegQ mediated proteolysis; PdeB variants which cannot form a disulphide bond in the periplasmic CSS domain have higher phosphodiesterase activity than the wild-type and interfere with macrocolony morphology when expressed in a cellulose and curli producing K-12 strain (AR3110) . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeB. This supports the view that many of the candidate c-di-GMP phosphodiesterases encoded in the E...

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52

## Incoming Edges (1)

- `encodes` <-- [[gene.b0457|gene.b0457]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77473`
- `KEGG:ecj:JW5062;eco:b0457;ecoc:C3026_02240;`
- `GeneID:948951;`
- `GO:GO:0005886; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeB (EC 3.1.4.52)
