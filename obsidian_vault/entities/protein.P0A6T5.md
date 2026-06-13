---
entity_id: "protein.P0A6T5"
entity_type: "protein"
name: "folE"
source_database: "UniProt"
source_id: "P0A6T5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folE b2153 JW2140"
---

# folE

`protein.P0A6T5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6T5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

GTP cyclohydrolase 1 (EC 3.5.4.16) (GTP cyclohydrolase I) (GTP-CH-I)

## Biological Role

Catalyzes GTP 7,8-8,9-dihydrolase (reaction.R00424), GTP 8,9-hydrolase (reaction.R00428). Component of GTP cyclohydrolase 1 (complex.ecocyc.FOLE-CPLX).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

GTP cyclohydrolase 1 (EC 3.5.4.16) (GTP cyclohydrolase I) (GTP-CH-I)

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00424|reaction.R00424]] `KEGG` `database` - via EC:3.5.4.16
- `catalyzes` --> [[reaction.R00428|reaction.R00428]] `KEGG` `database` - via EC:3.5.4.16
- `is_component_of` --> [[complex.ecocyc.FOLE-CPLX|complex.ecocyc.FOLE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b2153|gene.b2153]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6T5`
- `KEGG:ecj:JW2140;eco:b2153;ecoc:C3026_12065;`
- `GeneID:86860328;93775029;949040;`
- `GO:GO:0003934; GO:0005525; GO:0005737; GO:0005829; GO:0006729; GO:0006730; GO:0008270; GO:0008616; GO:0032991; GO:0042802; GO:0046654`
- `EC:3.5.4.16`

## Notes

GTP cyclohydrolase 1 (EC 3.5.4.16) (GTP cyclohydrolase I) (GTP-CH-I)
