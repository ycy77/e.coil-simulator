---
entity_id: "protein.P77445"
entity_type: "protein"
name: "eutE"
source_database: "UniProt"
source_id: "P77445"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000250|UniProtKB:P41793}. Note=Probably located inside the BMC. {ECO:0000250|UniProtKB:P41793}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutE yffX b2455 JW2439"
---

# eutE

`protein.P77445`

## Static

- Type: `protein`
- Source: `UniProt:P77445`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000250|UniProtKB:P41793}. Note=Probably located inside the BMC. {ECO:0000250|UniProtKB:P41793}.

## Enriched Summary

FUNCTION: Acts as the second step in ethanolamine degradation by converting acetaldehyde into acetyl-CoA. May play a role in bacterial microcompartment (BMC) assembly or maintenance. Directly targeted to the BMC (By similarity). Its heterologous expression in S.cerevisiae increases the level of acetylating acetaldehyde dehydrogenase activity (PubMed:26384570). {ECO:0000250|UniProtKB:P41793, ECO:0000269|PubMed:26384570}. Heterologous expression of EutE in various yeasts increases the level of acetylating acetaldehyde dehydrogenase activity in the cells and has been used in metabolic engineering .

## Biological Role

Catalyzes ACETALD-DEHYDROG-RXN (reaction.ecocyc.ACETALD-DEHYDROG-RXN).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Acts as the second step in ethanolamine degradation by converting acetaldehyde into acetyl-CoA. May play a role in bacterial microcompartment (BMC) assembly or maintenance. Directly targeted to the BMC (By similarity). Its heterologous expression in S.cerevisiae increases the level of acetylating acetaldehyde dehydrogenase activity (PubMed:26384570). {ECO:0000250|UniProtKB:P41793, ECO:0000269|PubMed:26384570}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2455|gene.b2455]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77445`
- `KEGG:ecj:JW2439;eco:b2455;ecoc:C3026_13625;`
- `GeneID:946943;`
- `GO:GO:0004029; GO:0008774; GO:0031469; GO:0046336`
- `EC:1.2.1.10`

## Notes

Acetaldehyde dehydrogenase (acetylating) EutE (EC 1.2.1.10) (Ethanolamine utilization protein EutE)
