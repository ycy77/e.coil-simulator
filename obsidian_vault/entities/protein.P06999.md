---
entity_id: "protein.P06999"
entity_type: "protein"
name: "pfkB"
source_database: "UniProt"
source_id: "P06999"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pfkB b1723 JW5280"
---

# pfkB

`protein.P06999`

## Static

- Type: `protein`
- Source: `UniProt:P06999`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis. {ECO:0000269|PubMed:16866375}.

## Biological Role

Catalyzes ATP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00756), CTP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00767), UTP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00769), ITP:D-fructose-6-phosphate 1-phosphotransferase (reaction.R00770). Component of 6-phosphofructokinase 2 (complex.ecocyc.6PFK-2-CPX).

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

## Annotation

FUNCTION: Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis. {ECO:0000269|PubMed:16866375}.

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

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00756|reaction.R00756]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` --> [[reaction.R00767|reaction.R00767]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` --> [[reaction.R00769|reaction.R00769]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` --> [[reaction.R00770|reaction.R00770]] `KEGG` `database` - via EC:2.7.1.11
- `is_component_of` --> [[complex.ecocyc.6PFK-2-CPX|complex.ecocyc.6PFK-2-CPX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1723|gene.b1723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06999`
- `KEGG:ecj:JW5280;eco:b1723;ecoc:C3026_09855;`
- `GeneID:946230;`
- `GO:GO:0000287; GO:0003872; GO:0005524; GO:0005829; GO:0006096; GO:0006974; GO:0009024; GO:0042802; GO:0042803`
- `EC:2.7.1.11`

## Notes

ATP-dependent 6-phosphofructokinase isozyme 2 (ATP-PFK 2) (Phosphofructokinase 2) (EC 2.7.1.11) (6-phosphofructokinase isozyme II) (Phosphohexokinase 2)
