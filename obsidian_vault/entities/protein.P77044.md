---
entity_id: "protein.P77044"
entity_type: "protein"
name: "mhpC"
source_database: "UniProt"
source_id: "P77044"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpC b0349 JW0340"
---

# mhpC

`protein.P77044`

## Static

- Type: `protein`
- Source: `UniProt:P77044`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of the C5-C6 bond of 2-hydroxy-6-oxononadienedioate and 2-hydroxy-6-oxononatrienedioate, a dienol ring fission product of the bacterial meta-cleavage pathway for degradation of phenylpropionic acid. MhpC shows some selectivity for the carboxylate of the side chain. {ECO:0000269|PubMed:15663941, ECO:0000269|PubMed:9098055, ECO:0000269|PubMed:9315862}.

## Biological Role

Catalyzes 2-hydroxy-6-oxonona-2,4-diene-1,9-dioate succinylhydrolase (reaction.R02603). Component of 2-hydroxy-6-oxononatrienedioate hydrolase (complex.ecocyc.CPLX0-7950).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of the C5-C6 bond of 2-hydroxy-6-oxononadienedioate and 2-hydroxy-6-oxononatrienedioate, a dienol ring fission product of the bacterial meta-cleavage pathway for degradation of phenylpropionic acid. MhpC shows some selectivity for the carboxylate of the side chain. {ECO:0000269|PubMed:15663941, ECO:0000269|PubMed:9098055, ECO:0000269|PubMed:9315862}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02603|reaction.R02603]] `KEGG` `database` - via EC:3.7.1.14
- `is_component_of` --> [[complex.ecocyc.CPLX0-7950|complex.ecocyc.CPLX0-7950]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0349|gene.b0349]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77044`
- `KEGG:ecj:JW0340;eco:b0349;ecoc:C3026_24880;`
- `GeneID:944954;`
- `GO:GO:0005737; GO:0016787; GO:0018771; GO:0019380; GO:0019622; GO:0042803; GO:0052823`
- `EC:3.7.1.14`

## Notes

2-hydroxy-6-oxononadienedioate/2-hydroxy-6-oxononatrienedioate hydrolase (EC 3.7.1.14) (2-hydroxy-6-ketonona-2,4-diene-1,9-dioic acid 5,6-hydrolase) (2-hydroxy-6-oxonona-2,4,7-triene-1,9-dioic acid 5,6-hydrolase) (2-hydroxy-6-oxonona-2,4-diene-1,9-dioic acid 5,6-hydrolase)
