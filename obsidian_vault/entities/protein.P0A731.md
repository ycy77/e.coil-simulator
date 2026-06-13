---
entity_id: "protein.P0A731"
entity_type: "protein"
name: "mgsA"
source_database: "UniProt"
source_id: "P0A731"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mgsA yccG b0963 JW5129"
---

# mgsA

`protein.P0A731`

## Static

- Type: `protein`
- Source: `UniProt:P0A731`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the formation of methylglyoxal from dihydroxyacetone phosphate. {ECO:0000255|HAMAP-Rule:MF_00549, ECO:0000269|PubMed:11389594, ECO:0000269|PubMed:15049687, ECO:0000269|PubMed:9665712}.

## Biological Role

Catalyzes glycerone-phosphate phosphate-lyase (methylglyoxal-forming) (reaction.R01016). Component of methylglyoxal synthase (complex.ecocyc.METHGLYSYN-CPLX).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of methylglyoxal from dihydroxyacetone phosphate. {ECO:0000255|HAMAP-Rule:MF_00549, ECO:0000269|PubMed:11389594, ECO:0000269|PubMed:15049687, ECO:0000269|PubMed:9665712}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01016|reaction.R01016]] `KEGG` `database` - via EC:4.2.3.3
- `is_component_of` --> [[complex.ecocyc.METHGLYSYN-CPLX|complex.ecocyc.METHGLYSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0963|gene.b0963]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A731`
- `KEGG:ecj:JW5129;eco:b0963;ecoc:C3026_05885;`
- `GeneID:93776451;945574;`
- `GO:GO:0005829; GO:0008929; GO:0019242; GO:0034214; GO:0042802`
- `EC:4.2.3.3`

## Notes

Methylglyoxal synthase (MGS) (EC 4.2.3.3)
