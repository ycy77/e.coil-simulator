---
entity_id: "protein.P0AGF6"
entity_type: "protein"
name: "tdcB"
source_database: "UniProt"
source_id: "P0AGF6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcB b3117 JW3088"
---

# tdcB

`protein.P0AGF6`

## Static

- Type: `protein`
- Source: `UniProt:P0AGF6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the anaerobic formation of alpha-ketobutyrate and ammonia from threonine in a two-step reaction. The first step involved a dehydration of threonine and a production of enamine intermediates (aminocrotonate), which tautomerizes to its imine form (iminobutyrate). Both intermediates are unstable and short-lived. The second step is the nonenzymatic hydrolysis of the enamine/imine intermediates to form 2-ketobutyrate and free ammonia. In the low water environment of the cell, the second step is accelerated by RidA. TdcB also dehydrates serine to yield pyruvate via analogous enamine/imine intermediates. {ECO:0000269|PubMed:10388709, ECO:0000269|PubMed:13405870, ECO:0000269|PubMed:15390404}.

## Biological Role

Catalyzes L-serine ammonia-lyase (reaction.R00220), L-threonine ammonia-lyase (2-oxobutanoate-forming) (reaction.R00996). Component of catabolic threonine dehydratase (complex.ecocyc.THREDEHYDCAT-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the anaerobic formation of alpha-ketobutyrate and ammonia from threonine in a two-step reaction. The first step involved a dehydration of threonine and a production of enamine intermediates (aminocrotonate), which tautomerizes to its imine form (iminobutyrate). Both intermediates are unstable and short-lived. The second step is the nonenzymatic hydrolysis of the enamine/imine intermediates to form 2-ketobutyrate and free ammonia. In the low water environment of the cell, the second step is accelerated by RidA. TdcB also dehydrates serine to yield pyruvate via analogous enamine/imine intermediates. {ECO:0000269|PubMed:10388709, ECO:0000269|PubMed:13405870, ECO:0000269|PubMed:15390404}.

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
- `is_component_of` --> [[complex.ecocyc.THREDEHYDCAT-CPLX|complex.ecocyc.THREDEHYDCAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3117|gene.b3117]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGF6`
- `KEGG:ecj:JW3088;eco:b3117;ecoc:C3026_17000;`
- `GeneID:75205074;947633;`
- `GO:GO:0000166; GO:0003941; GO:0004793; GO:0004794; GO:0005829; GO:0006565; GO:0006567; GO:0016597; GO:0030170; GO:0032991; GO:0070689`
- `EC:4.3.1.17; 4.3.1.19`

## Notes

L-threonine dehydratase catabolic TdcB (EC 4.3.1.19) (L-serine dehydratase) (EC 4.3.1.17) (Threonine deaminase)
