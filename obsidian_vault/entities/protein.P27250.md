---
entity_id: "protein.P27250"
entity_type: "protein"
name: "ahr"
source_database: "UniProt"
source_id: "P27250"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ahr yjgB b4269 JW5761"
---

# ahr

`protein.P27250`

## Static

- Type: `protein`
- Source: `UniProt:P27250`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of a wide range of aldehydes including aliphatic fatty aldehydes (C4-C16), into their corresponding alcohols. Has a strong preference for NADPH over NADH as the electron donor. Cannot use glyceraldehyde or a ketone as substrate. Is a relevant source of NADPH-dependent aldehyde reductase activity in E.coli. The in vivo functions of Ahr has yet to be determined. {ECO:0000269|PubMed:22731523, ECO:0000269|PubMed:23093176, ECO:0000269|PubMed:23248280}.

## Biological Role

Catalyzes primary_alcohol:NADP+ oxidoreductase (reaction.R00625), ethanol:NADP+ oxidoreductase (reaction.R00746), 6-hydroxyhexanoate:NADP+ oxidoreductase (reaction.R05231). Component of NADPH-dependent aldehyde reductase Ahr (complex.ecocyc.CPLX0-8549).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of a wide range of aldehydes including aliphatic fatty aldehydes (C4-C16), into their corresponding alcohols. Has a strong preference for NADPH over NADH as the electron donor. Cannot use glyceraldehyde or a ketone as substrate. Is a relevant source of NADPH-dependent aldehyde reductase activity in E.coli. The in vivo functions of Ahr has yet to be determined. {ECO:0000269|PubMed:22731523, ECO:0000269|PubMed:23093176, ECO:0000269|PubMed:23248280}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00625|reaction.R00625]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` --> [[reaction.R00746|reaction.R00746]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` --> [[reaction.R05231|reaction.R05231]] `KEGG` `database` - via EC:1.1.1.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8549|complex.ecocyc.CPLX0-8549]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4269|gene.b4269]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27250`
- `KEGG:ecj:JW5761;eco:b4269;ecoc:C3026_23025;`
- `GeneID:948802;`
- `GO:GO:0006631; GO:0008106; GO:0008270; GO:0016616; GO:0042803`
- `EC:1.1.1.2`

## Notes

Aldehyde reductase Ahr (EC 1.1.1.2) (Zinc-dependent alcohol dehydrogenase Ahr)
