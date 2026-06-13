---
entity_id: "protein.P21437"
entity_type: "protein"
name: "yggF"
source_database: "UniProt"
source_id: "P21437"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yggF yggK b2930 JW2897"
---

# yggF

`protein.P21437`

## Static

- Type: `protein`
- Source: `UniProt:P21437`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of fructose 1,6-bisphosphate to fructose 6-phosphate. Also displays a low activity toward glucose 1,6-bisphosphate, and no activity against ribulose 1,5-bisphosphate, fructose 2,6-bisphosphate, or fructose 1-phosphate. {ECO:0000269|PubMed:19073594}.

## Biological Role

Catalyzes D-fructose-1,6-bisphosphate 1-phosphohydrolase (reaction.R00762). Component of fructose 1,6-bisphosphatase YggF (complex.ecocyc.CPLX0-7776).

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

FUNCTION: Catalyzes the hydrolysis of fructose 1,6-bisphosphate to fructose 6-phosphate. Also displays a low activity toward glucose 1,6-bisphosphate, and no activity against ribulose 1,5-bisphosphate, fructose 2,6-bisphosphate, or fructose 1-phosphate. {ECO:0000269|PubMed:19073594}.

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
- `is_component_of` --> [[complex.ecocyc.CPLX0-7776|complex.ecocyc.CPLX0-7776]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2930|gene.b2930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21437`
- `KEGG:ecj:JW2897;eco:b2930;ecoc:C3026_16050;`
- `GeneID:947410;`
- `GO:GO:0006071; GO:0006094; GO:0030145; GO:0030388; GO:0042132`
- `EC:3.1.3.11`

## Notes

Fructose-1,6-bisphosphatase 2 class 2 (FBPase 2 class 2) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase 2 class 2)
