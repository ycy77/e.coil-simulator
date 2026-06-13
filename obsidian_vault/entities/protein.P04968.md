---
entity_id: "protein.P04968"
entity_type: "protein"
name: "ilvA"
source_database: "UniProt"
source_id: "P04968"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ilvA b3772 JW3745"
---

# ilvA

`protein.P04968`

## Static

- Type: `protein`
- Source: `UniProt:P04968`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the anaerobic formation of alpha-ketobutyrate and ammonia from threonine in a two-step reaction. The first step involved a dehydration of threonine and a production of enamine intermediates (aminocrotonate), which tautomerizes to its imine form (iminobutyrate). Both intermediates are unstable and short-lived. The second step is the nonenzymatic hydrolysis of the enamine/imine intermediates to form 2-ketobutyrate and free ammonia. In the low water environment of the cell, the second step is accelerated by RidA. {ECO:0000269|PubMed:13405870}.

## Biological Role

Catalyzes L-serine ammonia-lyase (reaction.R00220), L-threonine ammonia-lyase (2-oxobutanoate-forming) (reaction.R00996). Component of threonine deaminase (complex.ecocyc.THREDEHYDSYN-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the anaerobic formation of alpha-ketobutyrate and ammonia from threonine in a two-step reaction. The first step involved a dehydration of threonine and a production of enamine intermediates (aminocrotonate), which tautomerizes to its imine form (iminobutyrate). Both intermediates are unstable and short-lived. The second step is the nonenzymatic hydrolysis of the enamine/imine intermediates to form 2-ketobutyrate and free ammonia. In the low water environment of the cell, the second step is accelerated by RidA. {ECO:0000269|PubMed:13405870}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00220|reaction.R00220]] `KEGG` `database` - via EC:4.3.1.19
- `catalyzes` --> [[reaction.R00996|reaction.R00996]] `KEGG` `database` - via EC:4.3.1.19
- `is_component_of` --> [[complex.ecocyc.THREDEHYDSYN-CPLX|complex.ecocyc.THREDEHYDSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3772|gene.b3772]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04968`
- `KEGG:ecj:JW3745;eco:b3772;ecoc:C3026_20430;`
- `GeneID:948287;`
- `GO:GO:0004794; GO:0006566; GO:0009082; GO:0009097; GO:0016597; GO:0030170`
- `EC:4.3.1.19`

## Notes

L-threonine dehydratase biosynthetic IlvA (EC 4.3.1.19) (Threonine deaminase)
