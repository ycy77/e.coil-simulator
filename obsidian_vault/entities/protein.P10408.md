---
entity_id: "protein.P10408"
entity_type: "protein"
name: "secA"
source_database: "UniProt"
source_id: "P10408"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01382}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01382}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_01382}. Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01382}. Note=Distribution is 50-50. {ECO:0000255|HAMAP-Rule:MF_01382}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secA azi pea prlD b0098 JW0096"
---

# secA

`protein.P10408`

## Static

- Type: `protein`
- Source: `UniProt:P10408`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01382}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01382}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_01382}. Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01382}. Note=Distribution is 50-50. {ECO:0000255|HAMAP-Rule:MF_01382}.

## Enriched Summary

FUNCTION: Required for protein export, interacts with the SecYEG preprotein conducting channel. SecA has a central role in coupling the hydrolysis of ATP to the transfer of proteins into and across the cell membrane, serving both as a receptor for the preprotein-SecB complex and as an ATP-driven molecular motor driving the stepwise translocation of polypeptide chains across the membrane. {ECO:0000269|PubMed:10931320, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:1825804, ECO:0000269|PubMed:1830665, ECO:0000269|PubMed:2846186}.

## Biological Role

Component of SecYEG-SecA complex (complex.ecocyc.CPLX0-12269), protein translocation ATPase (complex.ecocyc.CPLX0-8089).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Required for protein export, interacts with the SecYEG preprotein conducting channel. SecA has a central role in coupling the hydrolysis of ATP to the transfer of proteins into and across the cell membrane, serving both as a receptor for the preprotein-SecB complex and as an ATP-driven molecular motor driving the stepwise translocation of polypeptide chains across the membrane. {ECO:0000269|PubMed:10931320, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:1825804, ECO:0000269|PubMed:1830665, ECO:0000269|PubMed:2846186}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12269|complex.ecocyc.CPLX0-12269]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8089|complex.ecocyc.CPLX0-8089]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0098|gene.b0098]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10408`
- `KEGG:ecj:JW0096;eco:b0098;ecoc:C3026_00395;`
- `GeneID:93777336;944821;`
- `GO:GO:0005524; GO:0005737; GO:0005886; GO:0006605; GO:0006612; GO:0008270; GO:0008564; GO:0009306; GO:0009898; GO:0015031; GO:0017038; GO:0031522; GO:0042802; GO:0043021; GO:0043022; GO:0043952; GO:0065002; GO:0070678`
- `EC:7.4.2.8`

## Notes

Protein translocase subunit SecA (EC 7.4.2.8)
