---
entity_id: "protein.P0A796"
entity_type: "protein"
name: "pfkA"
source_database: "UniProt"
source_id: "P0A796"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00339, ECO:0000305|PubMed:17895580}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pfkA b3916 JW3887"
---

# pfkA

`protein.P0A796`

## Static

- Type: `protein`
- Source: `UniProt:P0A796`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00339, ECO:0000305|PubMed:17895580}.

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis (PubMed:2953977, PubMed:3158524). In addition, is involved in the utilization of D-sedoheptulose 7-phosphate, an intermediate of the pentose phosphate pathway, via the sedoheptulose bisphosphate bypass pathway (PubMed:19756045). Catalyzes the phosphorylation of D-sedoheptulose 7-phosphate to D-sedoheptulose 1,7-bisphosphate (PubMed:19756045). {ECO:0000269|PubMed:19756045, ECO:0000269|PubMed:2953977, ECO:0000269|PubMed:3158524}.

## Biological Role

Catalyzes ATP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00756), CTP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00767), UTP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00769), ITP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00770). Component of 6-phosphofructokinase 1 (complex.ecocyc.6PFK-1-CPX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis (PubMed:2953977, PubMed:3158524). In addition, is involved in the utilization of D-sedoheptulose 7-phosphate, an intermediate of the pentose phosphate pathway, via the sedoheptulose bisphosphate bypass pathway (PubMed:19756045). Catalyzes the phosphorylation of D-sedoheptulose 7-phosphate to D-sedoheptulose 1,7-bisphosphate (PubMed:19756045). {ECO:0000269|PubMed:19756045, ECO:0000269|PubMed:2953977, ECO:0000269|PubMed:3158524}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00756|reaction.R00756]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` --> [[reaction.R00767|reaction.R00767]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` --> [[reaction.R00769|reaction.R00769]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` --> [[reaction.R00770|reaction.R00770]] `KEGG` `database` - via EC:2.7.1.11
- `is_component_of` --> [[complex.ecocyc.6PFK-1-CPX|complex.ecocyc.6PFK-1-CPX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3916|gene.b3916]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A796`
- `KEGG:ecj:JW3887;eco:b3916;ecoc:C3026_21170;`
- `GeneID:93777982;948412;`
- `GO:GO:0000287; GO:0003872; GO:0005524; GO:0005737; GO:0005829; GO:0005945; GO:0006002; GO:0006007; GO:0006096; GO:0019003; GO:0030388; GO:0032553; GO:0042802; GO:0051289; GO:0061621; GO:0070095`
- `EC:2.7.1.11`

## Notes

ATP-dependent 6-phosphofructokinase isozyme 1 (ATP-PFK 1) (Phosphofructokinase 1) (EC 2.7.1.11) (6-phosphofructokinase isozyme I) (Phosphohexokinase 1) (Sedoheptulose-7-phosphate kinase)
