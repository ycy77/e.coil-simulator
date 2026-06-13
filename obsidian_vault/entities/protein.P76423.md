---
entity_id: "protein.P76423"
entity_type: "protein"
name: "thiM"
source_database: "UniProt"
source_id: "P76423"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiM b2104 JW2091"
---

# thiM

`protein.P76423`

## Static

- Type: `protein`
- Source: `UniProt:P76423`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of the hydroxyl group of 4-methyl-5-beta-hydroxyethylthiazole (THZ). {ECO:0000255|HAMAP-Rule:MF_00228, ECO:0000269|PubMed:2542220}.

## Biological Role

Component of hydroxyethylthiazole kinase (complex.ecocyc.CPLX0-8211).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of the hydroxyl group of 4-methyl-5-beta-hydroxyethylthiazole (THZ). {ECO:0000255|HAMAP-Rule:MF_00228, ECO:0000269|PubMed:2542220}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8211|complex.ecocyc.CPLX0-8211]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2104|gene.b2104]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76423`
- `KEGG:ecj:JW2091;eco:b2104;ecoc:C3026_11805;`
- `GeneID:945142;`
- `GO:GO:0000287; GO:0004417; GO:0005524; GO:0005829; GO:0009229; GO:0036172; GO:0042802; GO:0052673`
- `EC:2.7.1.50`

## Notes

Hydroxyethylthiazole kinase (EC 2.7.1.50) (4-methyl-5-beta-hydroxyethylthiazole kinase) (TH kinase) (Thz kinase)
