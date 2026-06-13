---
entity_id: "protein.P78285"
entity_type: "protein"
name: "rrrD"
source_database: "UniProt"
source_id: "P78285"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rrrD arrD ybcS b0555 JW0544"
---

# rrrD

`protein.P78285`

## Static

- Type: `protein`
- Source: `UniProt:P78285`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Essential for lysis of bacterial cell wall, by showing cell wall hydrolyzing activity. Exhibits lytic activity against E.coli and S.typhi cell wall substrate. {ECO:0000269|PubMed:17914239}. RrrD is an endolysin encoded by the cryptic lambdoid prophage DLP12 . Overexpression of RrrD leads to lysis of the cells . The effect of an rrrD deletion on biofilm formation is dependent on the strain background. An rrrD mutant is impaired in curli-based biofilm formation, which may be an indirect effect due to altered peptidoglycan metabolism . Deletion of the lysis module of DLP12 defective prophage (essD, rrrD, rzpD/rzoD) induces an hypervesiculation phenotype (possibly due to an excess of PG fragments in the periplasmic space); expression of the module is sensitive to environmental stress factors (low temperature, high osmolarity and acidic pH) .

## Biological Role

Catalyzes 3.2.1.17-RXN (reaction.ecocyc.3.2.1.17-RXN).

## Annotation

FUNCTION: Essential for lysis of bacterial cell wall, by showing cell wall hydrolyzing activity. Exhibits lytic activity against E.coli and S.typhi cell wall substrate. {ECO:0000269|PubMed:17914239}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.2.1.17-RXN|reaction.ecocyc.3.2.1.17-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0555|gene.b0555]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P78285`
- `KEGG:ecj:JW0544;eco:b0555;ecoc:C3026_02745;`
- `GeneID:947539;`
- `GO:GO:0003796; GO:0009253; GO:0016998; GO:0042742; GO:0044659`
- `EC:3.2.1.17`

## Notes

Lysozyme RrrD (EC 3.2.1.17) (Endolysin) (Lysis protein) (Muramidase)
