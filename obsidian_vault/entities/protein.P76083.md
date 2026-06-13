---
entity_id: "protein.P76083"
entity_type: "protein"
name: "paaH"
source_database: "UniProt"
source_id: "P76083"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaH ydbU b1395 JW1390"
---

# paaH

`protein.P76083`

## Static

- Type: `protein`
- Source: `UniProt:P76083`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of 3-hydroxyadipyl-CoA to yield 3-oxoadipyl-CoA. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaH is the NAD+-dependent 3-hydroxyadipyl-CoA dehydrogenase involved in phenylacetate catabolism . A paaH mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaH: "phenylacetic acid degradation"

## Biological Role

Catalyzes (S)-3-hydroxyacyl-CoA:NAD+ oxidoreductase (reaction.R06941), RXN0-2044 (reaction.ecocyc.RXN0-2044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of 3-hydroxyadipyl-CoA to yield 3-oxoadipyl-CoA. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R06941|reaction.R06941]] `KEGG` `database` - via EC:1.1.1.157
- `catalyzes` --> [[reaction.ecocyc.RXN0-2044|reaction.ecocyc.RXN0-2044]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1395|gene.b1395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76083`
- `KEGG:ecj:JW1390;eco:b1395;ecoc:C3026_08140;`
- `GeneID:945940;`
- `GO:GO:0003857; GO:0006635; GO:0008691; GO:0010124; GO:0070403`
- `EC:1.1.1.-`

## Notes

3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.-)
