---
entity_id: "protein.P0AD61"
entity_type: "protein"
name: "pykF"
source_database: "UniProt"
source_id: "P0AD61"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pykF b1676 JW1666"
---

# pykF

`protein.P0AD61`

## Static

- Type: `protein`
- Source: `UniProt:P0AD61`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of pyruvate in the last step of glycolysis, it is irreversible under physiological conditions. The reaction is critical for the control of metabolic flux in the second part of glycolysis. {ECO:0000305|PubMed:8591049}.

## Biological Role

Catalyzes ATP:pyruvate 2-O-phosphotransferase (reaction.R00200), GTP:pyruvate 2-O-phosphotransferase (reaction.R00430), CTP:pyruvate 2-O-phosphotransferase (reaction.R00572), UTP:pyruvate 2-O-phosphotransferase (reaction.R00659), ITP:pyruvate 2-O-phosphotransferase (reaction.R00724), dATP:pyruvate 2-O-phosphotransferase (reaction.R01138). Component of pyruvate kinase 1 (complex.ecocyc.PKI-COMPLEX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of pyruvate in the last step of glycolysis, it is irreversible under physiological conditions. The reaction is critical for the control of metabolic flux in the second part of glycolysis. {ECO:0000305|PubMed:8591049}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R00200|reaction.R00200]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` --> [[reaction.R00430|reaction.R00430]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` --> [[reaction.R00572|reaction.R00572]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` --> [[reaction.R00659|reaction.R00659]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` --> [[reaction.R00724|reaction.R00724]] `KEGG` `database` - via EC:2.7.1.40
- `catalyzes` --> [[reaction.R01138|reaction.R01138]] `KEGG` `database` - via EC:2.7.1.40
- `is_component_of` --> [[complex.ecocyc.PKI-COMPLEX|complex.ecocyc.PKI-COMPLEX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1676|gene.b1676]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD61`
- `KEGG:ecj:JW1666;eco:b1676;ecoc:C3026_09605;`
- `GeneID:93775831;946179;`
- `GO:GO:0000287; GO:0004743; GO:0005524; GO:0005737; GO:0005829; GO:0006096; GO:0009408; GO:0016020; GO:0016301; GO:0030955; GO:0042802; GO:1902912`
- `EC:2.7.1.40`

## Notes

Pyruvate kinase I (EC 2.7.1.40) (PK-1)
