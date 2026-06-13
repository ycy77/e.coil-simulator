---
entity_id: "protein.Q46806"
entity_type: "protein"
name: "hyuA"
source_database: "UniProt"
source_id: "Q46806"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyuA ygeZ b2873 JW2841"
---

# hyuA

`protein.Q46806`

## Static

- Type: `protein`
- Source: `UniProt:Q46806`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the stereospecific hydrolysis of the cyclic amide bond of D-hydantoin derivatives with an aromatic side chains at the 5'-position. Has no activity on dihydropyrimidines. The physiological function is unknown. {ECO:0000269|PubMed:11092864}. Phenylhydantoinase is a novel enzyme exhibiting activity toward hydantoin derivatives with an aromatic side chain at the 5' position, with phenylhydantoin and hydroxyphenylhydantoin having the highest activity level. It is not active on dihydropyrimidines. The enzyme has a stereospecific preference for D-enantiomers. The physiological role of the enzyme is not yet known . HyuA has similarity to allantoinase enzymes , including AllB . The enzyme is a homotetramer . HyuA: hydantoin-utilizing enzyme A

## Biological Role

Catalyzes 5,6-dihydro-5-fluorouracil amidohydrolase (reaction.R08227). Component of phenylhydantoinase (complex.ecocyc.CPLX0-255).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the stereospecific hydrolysis of the cyclic amide bond of D-hydantoin derivatives with an aromatic side chains at the 5'-position. Has no activity on dihydropyrimidines. The physiological function is unknown. {ECO:0000269|PubMed:11092864}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08227|reaction.R08227]] `KEGG` `database` - via EC:3.5.2.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-255|complex.ecocyc.CPLX0-255]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2873|gene.b2873]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46806`
- `KEGG:ecj:JW2841;eco:b2873;ecoc:C3026_15760;`
- `GeneID:947359;`
- `GO:GO:0005829; GO:0006208; GO:0016812; GO:0042802; GO:0046872`
- `EC:3.5.2.-`

## Notes

D-phenylhydantoinase (EC 3.5.2.-) (Hydantoin-utilizing enzyme HyuA)
