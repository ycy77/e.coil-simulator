---
entity_id: "protein.P76237"
entity_type: "protein"
name: "dgcJ"
source_database: "UniProt"
source_id: "P76237"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcJ yeaJ b1786 JW5291"
---

# dgcJ

`protein.P76237`

## Static

- Type: `protein`
- Source: `UniProt:P76237`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}. DgcJ contains an N-terminal GAPES (GAmma-proteobacterial PEriplasmic Sensory) domain predicted to be periplasmic and a C-terminal cytoplasmic GGDEF domain with predicted diguanylate cyclase activity . DgcJ interacts directly with the C-DI-GMP-activated glycosyltransferase EG11739-MONOMER NfrB and is required for NfrAB-dependent phage N4 infection; DgcJ functions to provide cyclic di-3',5'-guanylate to NrfB wth resultant activation of glycosyltransferase activity . The periplasmic domain of DgcJ likely senses a nutritional signal . A dgcJ null mutant partially suppresses the loss of motility phenotype of a pdeH mutant at 37°C . Deletion of dgcJ increases swimming motility ; complementation by overexpressing dgcJ reduced swimming and swarming back to wild-type levels . dgcJ is expressed during exponential growth . DgcJ is active during vegetative growth at at 37°C; DgcJ, G7049-MONOMER DgcQ, and CPLX0-8535 DgcE all contribute to inhibiting motility of a ΔpdeH mutant at 37°C . Deletion of dgcJ provides strong protection against phage N4 . Kanamycin resistant (KR), dgcJ mutants were only obtained from wild-type cells plated on swarm media that crossed into Kan swim media (i.e...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1786|gene.b1786]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76237`
- `KEGG:ecj:JW5291;eco:b1786;ecoc:C3026_10185;`
- `GeneID:75203092;946290;`
- `GO:GO:0005525; GO:0005886; GO:0043709; GO:0046872; GO:0052621; GO:1902201`
- `EC:2.7.7.65`

## Notes

Probable diguanylate cyclase DgcJ (DGC) (EC 2.7.7.65)
