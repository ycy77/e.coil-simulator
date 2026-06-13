---
entity_id: "protein.P0AB71"
entity_type: "protein"
name: "fbaA"
source_database: "UniProt"
source_id: "P0AB71"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fbaA fba fda b2925 JW2892"
---

# fbaA

`protein.P0AB71`

## Static

- Type: `protein`
- Source: `UniProt:P0AB71`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to form fructose 1,6-bisphosphate (FBP) in gluconeogenesis and the reverse reaction in glycolysis (PubMed:10712619). In addition, is involved in the utilization of D-sedoheptulose 7-phosphate, an intermediate of the pentose phosphate pathway, via the sedoheptulose bisphosphate bypass pathway (PubMed:19756045). Catalyzes the cleavage of D-sedoheptulose 1,7-bisphosphate to glyceraldehyde 3-phosphate and erythrose 4-phosphate (PubMed:19756045). {ECO:0000269|PubMed:10712619, ECO:0000269|PubMed:19756045}.

## Biological Role

Component of fructose-bisphosphate aldolase class II (complex.ecocyc.FRUCBISALD-CLASSII).

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
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to form fructose 1,6-bisphosphate (FBP) in gluconeogenesis and the reverse reaction in glycolysis (PubMed:10712619). In addition, is involved in the utilization of D-sedoheptulose 7-phosphate, an intermediate of the pentose phosphate pathway, via the sedoheptulose bisphosphate bypass pathway (PubMed:19756045). Catalyzes the cleavage of D-sedoheptulose 1,7-bisphosphate to glyceraldehyde 3-phosphate and erythrose 4-phosphate (PubMed:19756045). {ECO:0000269|PubMed:10712619, ECO:0000269|PubMed:19756045}.

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
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FRUCBISALD-CLASSII|complex.ecocyc.FRUCBISALD-CLASSII]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2925|gene.b2925]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB71`
- `KEGG:ecj:JW2892;eco:b2925;ecoc:C3026_16025;`
- `GeneID:93779073;947415;`
- `GO:GO:0004332; GO:0005829; GO:0006094; GO:0006096; GO:0008270; GO:0042802; GO:0042803`
- `EC:4.1.2.13`

## Notes

Fructose-bisphosphate aldolase class 2 (FBP aldolase) (FBPA) (EC 4.1.2.13) (Fructose-1,6-bisphosphate aldolase) (Fructose-bisphosphate aldolase class II) (Sedoheptulose bisphosphate aldolase)
