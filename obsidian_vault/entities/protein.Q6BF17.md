---
entity_id: "protein.Q6BF17"
entity_type: "protein"
name: "dgoD"
source_database: "UniProt"
source_id: "Q6BF17"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgoD yidU b4478 JW5629"
---

# dgoD

`protein.Q6BF17`

## Static

- Type: `protein`
- Source: `UniProt:Q6BF17`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of D-galactonate to 2-keto-3-deoxy-D-galactonate. {ECO:0000269|PubMed:324806, ECO:0000269|Ref.7}. D-galactonate dehydratase catalyzes the first step in the degradation of D-galactonate, the dehydration of D-galactonate to form 2-dehydro-3-deoxygalactonate . D-galactonate dehydratase belongs to the mandelate racemase (MR) subgroup of the enolase superfamily . A reaction mechanism for the β-elimination of OH- involving His185 as a general acid/base catalyst has been proposed and is supported by analysis of point mutants . Production of galactonate dehydratase is induced by growth on galactonate . The inducer is D-galactonate, and expression is subject to catabolite repression . The enantiomer CPD-12349 alone cannot be used by E. coli as a sole carbon source, however a mixture of 2-dehydro-3-deoxy-L-galactonate and D-GALACTURONATE enables the utilization of both compounds .

## Biological Role

Catalyzes GALACTONDEHYDRAT-RXN (reaction.ecocyc.GALACTONDEHYDRAT-RXN), RXN-15893 (reaction.ecocyc.RXN-15893).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of D-galactonate to 2-keto-3-deoxy-D-galactonate. {ECO:0000269|PubMed:324806, ECO:0000269|Ref.7}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GALACTONDEHYDRAT-RXN|reaction.ecocyc.GALACTONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15893|reaction.ecocyc.RXN-15893]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4478|gene.b4478]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q6BF17`
- `KEGG:ecj:JW5629;eco:b4478;ecoc:C3026_20015;`
- `GeneID:2847765;75205406;`
- `GO:GO:0000287; GO:0008869; GO:0009063; GO:0016836; GO:0034194`
- `EC:4.2.1.6`

## Notes

D-galactonate dehydratase (GalD) (EC 4.2.1.6)
