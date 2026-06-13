---
entity_id: "protein.P0A858"
entity_type: "protein"
name: "tpiA"
source_database: "UniProt"
source_id: "P0A858"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00147, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tpiA tpi b3919 JW3890"
---

# tpiA

`protein.P0A858`

## Static

- Type: `protein`
- Source: `UniProt:P0A858`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00147, ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the gluconeogenesis. Catalyzes stereospecifically the conversion of dihydroxyacetone phosphate (DHAP) to D-glyceraldehyde-3-phosphate (G3P). {ECO:0000255|HAMAP-Rule:MF_00147, ECO:0000269|PubMed:9442062}.

## Biological Role

Catalyzes D-glyceraldehyde-3-phosphate aldose-ketose-isomerase (reaction.R01015). Component of triose-phosphate isomerase (complex.ecocyc.TPI).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the gluconeogenesis. Catalyzes stereospecifically the conversion of dihydroxyacetone phosphate (DHAP) to D-glyceraldehyde-3-phosphate (G3P). {ECO:0000255|HAMAP-Rule:MF_00147, ECO:0000269|PubMed:9442062}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01015|reaction.R01015]] `KEGG` `database` - via EC:5.3.1.1
- `is_component_of` --> [[complex.ecocyc.TPI|complex.ecocyc.TPI]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3919|gene.b3919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A858`
- `KEGG:ecj:JW3890;eco:b3919;ecoc:C3026_21185;`
- `GeneID:86861687;93777979;948409;`
- `GO:GO:0004807; GO:0005829; GO:0006094; GO:0006096; GO:0016020; GO:0019563; GO:0042802; GO:0046166`
- `EC:5.3.1.1`

## Notes

Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase)
