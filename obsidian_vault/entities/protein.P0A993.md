---
entity_id: "protein.P0A993"
entity_type: "protein"
name: "fbp"
source_database: "UniProt"
source_id: "P0A993"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01855, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fbp fdp b4232 JW4191"
---

# fbp

`protein.P0A993`

## Static

- Type: `protein`
- Source: `UniProt:P0A993`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01855, ECO:0000305}.

## Enriched Summary

Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1)

## Biological Role

Catalyzes D-fructose-1,6-bisphosphate 1-phosphohydrolase (reaction.R00762). Component of fructose-1,6-bisphosphatase 1 (complex.ecocyc.F16B-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1)

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00762|reaction.R00762]] `KEGG` `database` - via EC:3.1.3.11
- `is_component_of` --> [[complex.ecocyc.F16B-CPLX|complex.ecocyc.F16B-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b4232|gene.b4232]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A993`
- `KEGG:ecj:JW4191;eco:b4232;ecoc:C3026_22845;`
- `GeneID:86861371;948753;`
- `GO:GO:0000166; GO:0000287; GO:0005737; GO:0005829; GO:0006000; GO:0006002; GO:0006094; GO:0030388; GO:0032991; GO:0042132; GO:0042802`
- `EC:3.1.3.11`

## Notes

Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1)
