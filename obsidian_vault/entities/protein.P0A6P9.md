---
entity_id: "protein.P0A6P9"
entity_type: "protein"
name: "eno"
source_database: "UniProt"
source_id: "P0A6P9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000305|PubMed:4942326}. Cytoplasm, cytoskeleton {ECO:0000269|PubMed:17242352, ECO:0000269|PubMed:18337249}. Secreted {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000269|PubMed:15003462}. Cell surface {ECO:0000255|HAMAP-Rule:MF_00318}. Note=Fractions of enolase are present in both the cytoplasm and on the cell surface. As part of the bacterial cytoskeleton in the cytoplasm, is organized as extended coiled structures that wind around the cell, from one cell pole to the other (PubMed:17242352). When covalently bound to the substrate at Lys-342, the inactive enolase is secreted (PubMed:15003462). {ECO:0000269|PubMed:15003462, ECO:0000269|PubMed:17242352}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eno b2779 JW2750"
---

# eno

`protein.P0A6P9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6P9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000305|PubMed:4942326}. Cytoplasm, cytoskeleton {ECO:0000269|PubMed:17242352, ECO:0000269|PubMed:18337249}. Secreted {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000269|PubMed:15003462}. Cell surface {ECO:0000255|HAMAP-Rule:MF_00318}. Note=Fractions of enolase are present in both the cytoplasm and on the cell surface. As part of the bacterial cytoskeleton in the cytoplasm, is organized as extended coiled structures that wind around the cell, from one cell pole to the other (PubMed:17242352). When covalently bound to the substrate at Lys-342, the inactive enolase is secreted (PubMed:15003462). {ECO:0000269|PubMed:15003462, ECO:0000269|PubMed:17242352}.

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of 2-phosphoglycerate (2-PG) into phosphoenolpyruvate (PEP) (PubMed:2513001, PubMed:4942326). It is essential for the degradation of carbohydrates via glycolysis. {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000269|PubMed:2513001, ECO:0000269|PubMed:4942326}.; FUNCTION: Part of the RNA degradosome, a multi-enzyme complex involved in RNA processing and messenger RNA degradation (PubMed:8610017, PubMed:9732274). Its interaction with RNase E is important for the turnover of mRNA, in particular on transcripts encoding enzymes of energy-generating metabolic routes (PubMed:14981237). Its presence in the degradosome is required for the response to excess phosphosugar (PubMed:15522087). May play a regulatory role in the degradation of specific RNAs, such as ptsG mRNA, therefore linking cellular metabolic status with post-translational gene regulation (PubMed:15522087). {ECO:0000269|PubMed:14981237, ECO:0000269|PubMed:15522087, ECO:0000269|PubMed:17242352, ECO:0000269|PubMed:18337249, ECO:0000269|PubMed:8610017, ECO:0000269|PubMed:9732274}.

## Biological Role

Catalyzes 2-phospho-D-glycerate hydro-lyase (phosphoenolpyruvate-forming) (reaction.R00658). Component of degradosome (complex.ecocyc.CPLX0-2381), enolase (complex.ecocyc.ENOLASE-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible conversion of 2-phosphoglycerate (2-PG) into phosphoenolpyruvate (PEP) (PubMed:2513001, PubMed:4942326). It is essential for the degradation of carbohydrates via glycolysis. {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000269|PubMed:2513001, ECO:0000269|PubMed:4942326}.; FUNCTION: Part of the RNA degradosome, a multi-enzyme complex involved in RNA processing and messenger RNA degradation (PubMed:8610017, PubMed:9732274). Its interaction with RNase E is important for the turnover of mRNA, in particular on transcripts encoding enzymes of energy-generating metabolic routes (PubMed:14981237). Its presence in the degradosome is required for the response to excess phosphosugar (PubMed:15522087). May play a regulatory role in the degradation of specific RNAs, such as ptsG mRNA, therefore linking cellular metabolic status with post-translational gene regulation (PubMed:15522087). {ECO:0000269|PubMed:14981237, ECO:0000269|PubMed:15522087, ECO:0000269|PubMed:17242352, ECO:0000269|PubMed:18337249, ECO:0000269|PubMed:8610017, ECO:0000269|PubMed:9732274}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00658|reaction.R00658]] `KEGG` `database` - via EC:4.2.1.11
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.ENOLASE-CPLX|complex.ecocyc.ENOLASE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2779|gene.b2779]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6P9`
- `KEGG:ecj:JW2750;eco:b2779;ecoc:C3026_15270;`
- `GeneID:86860869;93779219;945032;`
- `GO:GO:0000015; GO:0000287; GO:0004634; GO:0005576; GO:0005829; GO:0005856; GO:0006096; GO:0006396; GO:0006401; GO:0009986; GO:0016020; GO:0042802; GO:0042803; GO:1990061`
- `EC:4.2.1.11`

## Notes

Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase)
