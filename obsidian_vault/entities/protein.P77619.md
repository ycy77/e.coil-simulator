---
entity_id: "protein.P77619"
entity_type: "protein"
name: "yfeW"
source_database: "UniProt"
source_id: "P77619"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01034, ECO:0000305|PubMed:16402224}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01034, ECO:0000305|PubMed:16402224}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfeW pbp4B b2430 JW5395"
---

# yfeW

`protein.P77619`

## Static

- Type: `protein`
- Source: `UniProt:P77619`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01034, ECO:0000305|PubMed:16402224}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01034, ECO:0000305|PubMed:16402224}.

## Enriched Summary

FUNCTION: Penicillin-binding protein. Has low DD-carboxypeptidase activity. {ECO:0000269|PubMed:16402224}. Purified YfeW can bind penicillin and displays a low level of DD-carboxypeptidase activity . yfeW is non-essential . MurQP-yfeW may constitute an operon in E. coli K-12 . Deleting yfeW does not affect growth on N-acetylmuramic acid .

## Biological Role

Catalyzes RXN-16649 (reaction.ecocyc.RXN-16649).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Penicillin-binding protein. Has low DD-carboxypeptidase activity. {ECO:0000269|PubMed:16402224}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2430|gene.b2430]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77619`
- `KEGG:ecj:JW5395;eco:b2430;ecoc:C3026_13500;`
- `GeneID:946907;`
- `GO:GO:0005886; GO:0006508; GO:0008658; GO:0009002`
- `EC:3.4.16.4`

## Notes

Putative D-alanyl-D-alanine carboxypeptidase (EC 3.4.16.4) (DD-carboxypeptidase) (DD-CPase) (Penicillin binding protein 4B)
