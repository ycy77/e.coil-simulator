---
entity_id: "protein.P04693"
entity_type: "protein"
name: "tyrB"
source_database: "UniProt"
source_id: "P04693"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tyrB b4054 JW4014"
---

# tyrB

`protein.P04693`

## Static

- Type: `protein`
- Source: `UniProt:P04693`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Broad-specificity enzyme that catalyzes the transamination of 2-ketoisocaproate, p-hydroxyphenylpyruvate, and phenylpyruvate to yield leucine, tyrosine, and phenylalanine, respectively. In vitro, is able to catalyze the conversion of beta-methyl phenylpyruvate to the nonproteinogenic amino acid (2S,3S)-beta-methyl-phenylalanine, a building block of the antibiotic mannopeptimycin produced by Streptomyces hygroscopicus NRRL3085. {ECO:0000269|PubMed:19731276}.

## Biological Role

Catalyzes L-phenylalanine:2-oxoglutarate aminotransferase (reaction.R00694), L-tyrosine:2-oxoglutarate aminotransferase (reaction.R00734), L-arogenate:2-oxoglutarate aminotransferase (reaction.R01731). Component of tyrosine aminotransferase (complex.ecocyc.TYRB-DIMER).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Broad-specificity enzyme that catalyzes the transamination of 2-ketoisocaproate, p-hydroxyphenylpyruvate, and phenylpyruvate to yield leucine, tyrosine, and phenylalanine, respectively. In vitro, is able to catalyze the conversion of beta-methyl phenylpyruvate to the nonproteinogenic amino acid (2S,3S)-beta-methyl-phenylalanine, a building block of the antibiotic mannopeptimycin produced by Streptomyces hygroscopicus NRRL3085. {ECO:0000269|PubMed:19731276}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - via EC:2.6.1.57
- `catalyzes` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - via EC:2.6.1.57
- `catalyzes` --> [[reaction.R01731|reaction.R01731]] `KEGG` `database` - via EC:2.6.1.57
- `is_component_of` --> [[complex.ecocyc.TYRB-DIMER|complex.ecocyc.TYRB-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4054|gene.b4054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04693`
- `KEGG:ecj:JW4014;eco:b4054;ecoc:C3026_21905;`
- `GeneID:948563;`
- `GO:GO:0004838; GO:0005737; GO:0005829; GO:0006532; GO:0008793; GO:0009098; GO:0019292; GO:0030170; GO:0033585; GO:0042802; GO:0042803; GO:0052654`
- `EC:2.6.1.107; 2.6.1.57`

## Notes

Aromatic-amino-acid aminotransferase (ARAT) (AROAT) (EC 2.6.1.57) (Beta-methylphenylalanine transaminase) (EC 2.6.1.107)
