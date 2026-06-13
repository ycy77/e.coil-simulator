---
entity_id: "protein.P76085"
entity_type: "protein"
name: "paaK"
source_database: "UniProt"
source_id: "P76085"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaK b1398 JW5218"
---

# paaK

`protein.P76085`

## Static

- Type: `protein`
- Source: `UniProt:P76085`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the activation of phenylacetic acid (PA) to phenylacetyl-CoA (PA-CoA). {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaK has been shown to have phenylacetate-CoA ligase activity in E. coli W. There, the enzyme catalyzes the first step in an aerobic pathway of phenylacetate degradation . Additional steps in the phenylacetate degradation pathway have been predicted and recently experimentally studied . Some, but not all, E. coli K-12 strains are able to utilize phenylacetate as the sole source of carbon and energy. The E. coli K-12 strains MG1655 and W3110 as well as E. coli W exhibit utilization, while E. coli C does not exhibit utilization due to deletion of a large fragment that includes the paa region . PaaK: "phenylacetic acid degradation"

## Biological Role

Catalyzes RXN-10819 (reaction.ecocyc.RXN-10819).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the activation of phenylacetic acid (PA) to phenylacetyl-CoA (PA-CoA). {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-10819|reaction.ecocyc.RXN-10819]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1398|gene.b1398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76085`
- `KEGG:ecj:JW5218;eco:b1398;ecoc:C3026_08155;`
- `GeneID:945963;`
- `GO:GO:0005524; GO:0010124; GO:0016405; GO:0047475`
- `EC:6.2.1.30`

## Notes

Phenylacetate-coenzyme A ligase (EC 6.2.1.30) (Phenylacetyl-CoA ligase) (PA-CoA ligase)
