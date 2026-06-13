---
entity_id: "protein.P21599"
entity_type: "protein"
name: "pykA"
source_database: "UniProt"
source_id: "P21599"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pykA b1854 JW1843"
---

# pykA

`protein.P21599`

## Static

- Type: `protein`
- Source: `UniProt:P21599`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of pyruvate in the last step of glycolysis, it is irreversible under physiological conditions. The reaction is critical for the control of metabolic flux in the second part of glycolysis. {ECO:0000305}.

## Biological Role

Catalyzes ATP:pyruvate 2-O-phosphotransferase (reaction.R00200), GTP:pyruvate 2-O-phosphotransferase (reaction.R00430), CTP:pyruvate 2-O-phosphotransferase (reaction.R00572), UTP:pyruvate 2-O-phosphotransferase (reaction.R00659), ITP:pyruvate 2-O-phosphotransferase (reaction.R00724), dATP:pyruvate 2-O-phosphotransferase (reaction.R01138). Component of pyruvate kinase 2 (complex.ecocyc.PKII-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of pyruvate in the last step of glycolysis, it is irreversible under physiological conditions. The reaction is critical for the control of metabolic flux in the second part of glycolysis. {ECO:0000305}.

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
- `is_component_of` --> [[complex.ecocyc.PKII-CPLX|complex.ecocyc.PKII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1854|gene.b1854]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21599`
- `KEGG:ecj:JW1843;eco:b1854;ecoc:C3026_10565;`
- `GeneID:93776121;946527;`
- `GO:GO:0000287; GO:0004743; GO:0005524; GO:0005737; GO:0005829; GO:0006096; GO:0016208; GO:0016301; GO:0030955; GO:0042802; GO:1902912`
- `EC:2.7.1.40`

## Notes

Pyruvate kinase II (EC 2.7.1.40) (PK-2)
