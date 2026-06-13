---
entity_id: "protein.P77671"
entity_type: "protein"
name: "allB"
source_database: "UniProt"
source_id: "P77671"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allB glxB3 ybbX b0512 JW0500"
---

# allB

`protein.P77671`

## Static

- Type: `protein`
- Source: `UniProt:P77671`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of allantoin (5-ureidohydantoin) to allantoic acid by hydrolytic cleavage of the five-member hydantoin ring. {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:11092864}.

## Biological Role

Component of allantoinase (complex.ecocyc.CPLX-64).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of allantoin (5-ureidohydantoin) to allantoic acid by hydrolytic cleavage of the five-member hydantoin ring. {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:11092864}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.TRANS-RXN0-444|reaction.ecocyc.TRANS-RXN0-444]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX-64|complex.ecocyc.CPLX-64]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0512|gene.b0512]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77671`
- `KEGG:ecj:JW0500;eco:b0512;ecoc:C3026_02510;`
- `GeneID:945134;`
- `GO:GO:0004038; GO:0005737; GO:0006145; GO:0008270; GO:0009442; GO:0050897`
- `EC:3.5.2.5`

## Notes

Allantoinase (EC 3.5.2.5) (Allantoin-utilizing enzyme)
