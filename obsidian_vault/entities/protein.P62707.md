---
entity_id: "protein.P62707"
entity_type: "protein"
name: "gpmA"
source_database: "UniProt"
source_id: "P62707"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gpmA gpm pgm pgmA b0755 JW0738"
---

# gpmA

`protein.P62707`

## Static

- Type: `protein`
- Source: `UniProt:P62707`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion of 2-phosphoglycerate and 3-phosphoglycerate. {ECO:0000255|HAMAP-Rule:MF_01039, ECO:0000269|PubMed:10437801}.

## Biological Role

Catalyzes D-phosphoglycerate 2,3-phosphomutase (reaction.R01518). Component of 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase (complex.ecocyc.PHOSGLYCMUTASE).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of 2-phosphoglycerate and 3-phosphoglycerate. {ECO:0000255|HAMAP-Rule:MF_01039, ECO:0000269|PubMed:10437801}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01518|reaction.R01518]] `KEGG` `database` - via EC:5.4.2.11
- `is_component_of` --> [[complex.ecocyc.PHOSGLYCMUTASE|complex.ecocyc.PHOSGLYCMUTASE]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0755|gene.b0755]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62707`
- `KEGG:ecj:JW0738;eco:b0755;ecoc:C3026_03820;`
- `GeneID:86863265;93776726;945068;`
- `GO:GO:0004619; GO:0005524; GO:0005737; GO:0005829; GO:0006094; GO:0042803; GO:0061621; GO:0097216`
- `EC:5.4.2.11`

## Notes

2,3-bisphosphoglycerate-dependent phosphoglycerate mutase (BPG-dependent PGAM) (PGAM) (Phosphoglyceromutase) (dPGM) (EC 5.4.2.11)
