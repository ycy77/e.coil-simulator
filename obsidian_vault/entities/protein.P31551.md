---
entity_id: "protein.P31551"
entity_type: "protein"
name: "caiD"
source_database: "UniProt"
source_id: "P31551"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "caiD yaaL b0036 JW0035"
---

# caiD

`protein.P31551`

## Static

- Type: `protein`
- Source: `UniProt:P31551`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible dehydration of L-carnitinyl-CoA to crotonobetainyl-CoA (PubMed:11551212). Can also hydrate crotonyl-CoA to hydroxybutyryl-CoA (PubMed:11551212). {ECO:0000269|PubMed:11551212}. CaiD is a member of the crotonase superfamily; the enzyme purified from E. coli O44:K74 catalyzes the hydration of crotonobetainyl-CoA to carnitinyl-CoA and can use crotonyl-CoA, but not crotonobetaine, as an alternative substrate . CaiD was originally also described as a carnitine racemase; however, only overexpressing both CaiD and CaiE together led to measurable carnitine racemase activity .

## Biological Role

Catalyzes CARNDETRU-RXN (reaction.ecocyc.CARNDETRU-RXN).

## Annotation

FUNCTION: Catalyzes the reversible dehydration of L-carnitinyl-CoA to crotonobetainyl-CoA (PubMed:11551212). Can also hydrate crotonyl-CoA to hydroxybutyryl-CoA (PubMed:11551212). {ECO:0000269|PubMed:11551212}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CARNDETRU-RXN|reaction.ecocyc.CARNDETRU-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0036|gene.b0036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31551`
- `KEGG:ecj:JW0035;eco:b0036;ecoc:C3026_00190;`
- `GeneID:948995;`
- `GO:GO:0006635; GO:0008735; GO:0008809; GO:0042413; GO:0120092`
- `EC:4.2.1.149`

## Notes

Carnitinyl-CoA dehydratase (EC 4.2.1.149) (Crotonobetainyl-CoA hydratase)
