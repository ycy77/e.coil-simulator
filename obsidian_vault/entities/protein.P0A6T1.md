---
entity_id: "protein.P0A6T1"
entity_type: "protein"
name: "pgi"
source_database: "UniProt"
source_id: "P0A6T1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00473, ECO:0000269|PubMed:4344919}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgi b4025 JW3985"
---

# pgi

`protein.P0A6T1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6T1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00473, ECO:0000269|PubMed:4344919}.

## Enriched Summary

FUNCTION: Catalyzes the reversible isomerization of glucose-6-phosphate to fructose-6-phosphate. {ECO:0000255|HAMAP-Rule:MF_00473}.

## Biological Role

Catalyzes D-glucose-6-phosphate aldose-ketose-isomerase (reaction.R00771). Component of glucose-6-phosphate isomerase (complex.ecocyc.CPLX0-7877).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible isomerization of glucose-6-phosphate to fructose-6-phosphate. {ECO:0000255|HAMAP-Rule:MF_00473}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00771|reaction.R00771]] `KEGG` `database` - via EC:5.3.1.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-7877|complex.ecocyc.CPLX0-7877]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4025|gene.b4025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6T1`
- `KEGG:ecj:JW3985;eco:b4025;ecoc:C3026_21740;`
- `GeneID:93777863;948535;`
- `GO:GO:0004347; GO:0005829; GO:0006094; GO:0006096; GO:0034599; GO:0042802; GO:0042803; GO:0048029; GO:0051156; GO:0097367`
- `EC:5.3.1.9`

## Notes

Glucose-6-phosphate isomerase (GPI) (EC 5.3.1.9) (Phosphoglucose isomerase) (PGI) (Phosphohexose isomerase) (PHI)
