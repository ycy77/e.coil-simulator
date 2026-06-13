---
entity_id: "protein.P32718"
entity_type: "protein"
name: "alsK"
source_database: "UniProt"
source_id: "P32718"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alsK yjcT b4084 JW5724"
---

# alsK

`protein.P32718`

## Static

- Type: `protein`
- Source: `UniProt:P32718`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of D-allose to D-allose 6-phosphate. Also has low level glucokinase activity in vitro. {ECO:0000255|HAMAP-Rule:MF_00988, ECO:0000269|PubMed:17979299, ECO:0000269|PubMed:9401019}. The alsK gene encodes a D-allose kinase. Its role in the degradation of D-allose is unclear; AlsK is not required for utilization of a D-allose carbon source; this effect may be due to the presence of other ambiguous sugar kinases within E. coli K-12 . Expression of alsK appears to be unaffected by allose . Overexpression of alsK rescues the auxotrophic phenotype of a glucokinase mutant . The low glucokinase activity of AlsK can be improved by experimental evolution . Als: "D-allose"

## Biological Role

Catalyzes ALLOSE-KINASE-RXN (reaction.ecocyc.ALLOSE-KINASE-RXN).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of D-allose to D-allose 6-phosphate. Also has low level glucokinase activity in vitro. {ECO:0000255|HAMAP-Rule:MF_00988, ECO:0000269|PubMed:17979299, ECO:0000269|PubMed:9401019}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALLOSE-KINASE-RXN|reaction.ecocyc.ALLOSE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4084|gene.b4084]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32718`
- `KEGG:ecj:JW5724;eco:b4084;ecoc:C3026_22080;`
- `GeneID:948596;`
- `GO:GO:0004340; GO:0004396; GO:0005524; GO:0008787; GO:0019316`
- `EC:2.7.1.55`

## Notes

D-allose kinase (Allokinase) (EC 2.7.1.55)
