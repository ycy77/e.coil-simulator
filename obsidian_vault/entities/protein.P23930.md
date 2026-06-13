---
entity_id: "protein.P23930"
entity_type: "protein"
name: "lnt"
source_database: "UniProt"
source_id: "P23930"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01148, ECO:0000269|PubMed:15513925, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2032623, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01148, ECO:0000269|PubMed:15513925, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lnt cutE b0657 JW0654"
---

# lnt

`protein.P23930`

## Static

- Type: `protein`
- Source: `UniProt:P23930`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01148, ECO:0000269|PubMed:15513925, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2032623, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01148, ECO:0000269|PubMed:15513925, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614}.

## Enriched Summary

FUNCTION: Catalyzes the phospholipid dependent N-acylation of the N-terminal cysteine of apolipoprotein, the last step in lipoprotein maturation (PubMed:2032623, PubMed:21676878, PubMed:28675161, PubMed:28885614). Utilizes a two-step reaction via a ping-pong mechanism (PubMed:21676878, PubMed:28675161). Lnt undergoes covalent modification in the presence of phospholipids, resulting in a thioester acyl-enzyme intermediate. It then transfers the acyl chain to the amine group of the N-terminal diacylglyceryl-modified cysteine of apolipoprotein, leading to the formation of mature triacylated lipoprotein (PubMed:21676878, PubMed:28675161). In vitro, can utilize the phospholipids phosphatidylethanolamine (PE), phosphatidylglycerol (PG), phosphatidic acid (PA) or cardiolipin (CL) (PubMed:2032623, PubMed:21676878). PE is the most efficient acyl donor (PubMed:21676878). {ECO:0000269|PubMed:2032623, ECO:0000269|PubMed:21676878, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614, ECO:0000305|PubMed:8344936}. Apolipoprotein N-acyltransferase catalyses the last step in lipoprotein maturation: the transfer of a fatty acid from phospholipid to the amino terminus of a diacylglycerol prolipoprotein...

## Biological Role

Catalyzes RXN-17363 (reaction.ecocyc.RXN-17363), RXN-19774 (reaction.ecocyc.RXN-19774).

## Annotation

FUNCTION: Catalyzes the phospholipid dependent N-acylation of the N-terminal cysteine of apolipoprotein, the last step in lipoprotein maturation (PubMed:2032623, PubMed:21676878, PubMed:28675161, PubMed:28885614). Utilizes a two-step reaction via a ping-pong mechanism (PubMed:21676878, PubMed:28675161). Lnt undergoes covalent modification in the presence of phospholipids, resulting in a thioester acyl-enzyme intermediate. It then transfers the acyl chain to the amine group of the N-terminal diacylglyceryl-modified cysteine of apolipoprotein, leading to the formation of mature triacylated lipoprotein (PubMed:21676878, PubMed:28675161). In vitro, can utilize the phospholipids phosphatidylethanolamine (PE), phosphatidylglycerol (PG), phosphatidic acid (PA) or cardiolipin (CL) (PubMed:2032623, PubMed:21676878). PE is the most efficient acyl donor (PubMed:21676878). {ECO:0000269|PubMed:2032623, ECO:0000269|PubMed:21676878, ECO:0000269|PubMed:28675161, ECO:0000269|PubMed:28885614, ECO:0000305|PubMed:8344936}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17363|reaction.ecocyc.RXN-17363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19774|reaction.ecocyc.RXN-19774]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0657|gene.b0657]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23930`
- `KEGG:ecj:JW0654;eco:b0657;ecoc:C3026_03285;`
- `GeneID:946201;`
- `GO:GO:0005886; GO:0016410; GO:0030288; GO:0042158`
- `EC:2.3.1.269`

## Notes

Apolipoprotein N-acyltransferase (ALP N-acyltransferase) (EC 2.3.1.269) (Copper homeostasis protein CutE)
