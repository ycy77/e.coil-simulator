---
entity_id: "protein.P09831"
entity_type: "protein"
name: "gltB"
source_database: "UniProt"
source_id: "P09831"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltB aspB b3212 JW3179"
---

# gltB

`protein.P09831`

## Static

- Type: `protein`
- Source: `UniProt:P09831`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of L-glutamine and 2-oxoglutarate into two molecules of L-glutamate. {ECO:0000269|PubMed:4565085}.

## Biological Role

Catalyzes L-glutamate:NADP+ oxidoreductase (transaminating) (reaction.R00114), L-glutamate:NADP+ oxidoreductase (deaminating) (reaction.R00248), L-glutamine amidohydrolase (reaction.R00256). Component of glutamate synthase (complex.ecocyc.GLUTAMATESYN-CPLX), glutamate synthase (complex.ecocyc.GLUTAMATESYN-DIMER).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of L-glutamine and 2-oxoglutarate into two molecules of L-glutamate. {ECO:0000269|PubMed:4565085}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00114|reaction.R00114]] `KEGG` `database` - via EC:1.4.1.13
- `catalyzes` --> [[reaction.R00248|reaction.R00248]] `KEGG` `database` - via EC:1.4.1.13
- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:1.4.1.13
- `is_component_of` --> [[complex.ecocyc.GLUTAMATESYN-CPLX|complex.ecocyc.GLUTAMATESYN-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.GLUTAMATESYN-DIMER|complex.ecocyc.GLUTAMATESYN-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3212|gene.b3212]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09831`
- `KEGG:ecj:JW3179;eco:b3212;ecoc:C3026_17475;`
- `GeneID:947724;`
- `GO:GO:0004355; GO:0005829; GO:0006537; GO:0009342; GO:0015930; GO:0019676; GO:0046872; GO:0051538; GO:0097054`
- `EC:1.4.1.13`

## Notes

Glutamate synthase [NADPH] large chain (EC 1.4.1.13) (Glutamate synthase subunit alpha) (GLTS alpha chain) (NADPH-GOGAT)
