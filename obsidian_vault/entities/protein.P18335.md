---
entity_id: "protein.P18335"
entity_type: "protein"
name: "argD"
source_database: "UniProt"
source_id: "P18335"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01107, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argD dapC dtu b3359 JW3322"
---

# argD

`protein.P18335`

## Static

- Type: `protein`
- Source: `UniProt:P18335`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01107, ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in both the arginine and lysine biosynthetic pathways. {ECO:0000255|HAMAP-Rule:MF_01107, ECO:0000269|PubMed:10074354}.

## Biological Role

Component of N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase (complex.ecocyc.ACETYLORNTRANSAM-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in both the arginine and lysine biosynthetic pathways. {ECO:0000255|HAMAP-Rule:MF_01107, ECO:0000269|PubMed:10074354}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ACETYLORNTRANSAM-CPLX|complex.ecocyc.ACETYLORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3359|gene.b3359]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18335`
- `KEGG:ecj:JW3322;eco:b3359;ecoc:C3026_18245;`
- `GeneID:947864;`
- `GO:GO:0003992; GO:0005737; GO:0009016; GO:0030170; GO:0033359; GO:0042450; GO:0042802; GO:0043648`
- `EC:2.6.1.11; 2.6.1.17`

## Notes

Acetylornithine/succinyldiaminopimelate aminotransferase (ACOAT) (DapATase) (Succinyldiaminopimelate transferase) (EC 2.6.1.11) (EC 2.6.1.17)
