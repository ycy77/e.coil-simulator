---
entity_id: "protein.P0C7L2"
entity_type: "protein"
name: "paaJ"
source_database: "UniProt"
source_id: "P0C7L2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaJ paaE ydbW b1397 JW1392"
---

# paaJ

`protein.P0C7L2`

## Static

- Type: `protein`
- Source: `UniProt:P0C7L2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the thiolytic cleavage of the beta-keto C8 intermediate 3-oxo-5,6-dehydrosuberyl-CoA with CoA to yield the C6 intermediate 2,3-dehydroadipyl-CoA and acetyl-CoA. Besides it catalyzes also the last step of the pathway, in which 3-oxoadipyl-CoA similarly is cleaved to acetyl-CoA and succinyl-CoA. {ECO:0000269|PubMed:17259607, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaJ is a β-ketoadipyl-CoA thiolase catalyzing two steps in phenylacetate catabolism . A paaJ mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaJ: "phenylacetic acid degradation" Review, including new consensus gene names:

## Biological Role

Catalyzes succinyl-CoA:acetyl-CoA C-acyltransferase; (reaction.R00829), RXN-3641 (reaction.ecocyc.RXN-3641), RXN0-6512 (reaction.ecocyc.RXN0-6512).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the thiolytic cleavage of the beta-keto C8 intermediate 3-oxo-5,6-dehydrosuberyl-CoA with CoA to yield the C6 intermediate 2,3-dehydroadipyl-CoA and acetyl-CoA. Besides it catalyzes also the last step of the pathway, in which 3-oxoadipyl-CoA similarly is cleaved to acetyl-CoA and succinyl-CoA. {ECO:0000269|PubMed:17259607, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00829|reaction.R00829]] `KEGG` `database` - via EC:2.3.1.174
- `catalyzes` --> [[reaction.ecocyc.RXN-3641|reaction.ecocyc.RXN-3641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6512|reaction.ecocyc.RXN0-6512]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1397|gene.b1397]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C7L2`
- `KEGG:ecj:JW1392;eco:b1397;ecoc:C3026_08150;`
- `GeneID:946121;`
- `GO:GO:0003988; GO:0006635; GO:0006974; GO:0010124; GO:0016740; GO:0019619; GO:0033812`
- `EC:2.3.1.174; 2.3.1.223`

## Notes

3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase (EC 2.3.1.174) (EC 2.3.1.223)
