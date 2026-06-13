---
entity_id: "protein.P27829"
entity_type: "protein"
name: "wecC"
source_database: "UniProt"
source_id: "P27829"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecC rffD b3787 JW5599"
---

# wecC

`protein.P27829`

## Static

- Type: `protein`
- Source: `UniProt:P27829`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the four-electron oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc), reducing NAD(+) and releasing UDP-N-acetylmannosaminuronic acid (UDP-ManNAcA). {ECO:0000255|HAMAP-Rule:MF_02029, ECO:0000269|PubMed:381306}.

## Biological Role

Component of UDP-N-acetyl-D-mannosamine dehydrogenase (complex.ecocyc.CPLX0-8013).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Catalyzes the four-electron oxidation of UDP-N-acetyl-D-mannosamine (UDP-ManNAc), reducing NAD(+) and releasing UDP-N-acetylmannosaminuronic acid (UDP-ManNAcA). {ECO:0000255|HAMAP-Rule:MF_02029, ECO:0000269|PubMed:381306}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8013|complex.ecocyc.CPLX0-8013]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3787|gene.b3787]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27829`
- `KEGG:ecj:JW5599;eco:b3787;ecoc:C3026_20505;`
- `GeneID:75174019;948977;`
- `GO:GO:0000271; GO:0005829; GO:0009246; GO:0016491; GO:0016628; GO:0042803; GO:0051287; GO:0089714`
- `EC:1.1.1.336`

## Notes

UDP-N-acetyl-D-mannosamine dehydrogenase (EC 1.1.1.336) (UDP-ManNAc 6-dehydrogenase)
