---
entity_id: "protein.P00509"
entity_type: "protein"
name: "aspC"
source_database: "UniProt"
source_id: "P00509"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aspC b0928 JW0911"
---

# aspC

`protein.P00509`

## Static

- Type: `protein`
- Source: `UniProt:P00509`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Aspartate aminotransferase (AspAT) (EC 2.6.1.1) (Transaminase A)

## Biological Role

Catalyzes L-aspartate:2-oxoglutarate aminotransferase (reaction.R00355), L-phenylalanine:2-oxoglutarate aminotransferase (reaction.R00694), L-tyrosine:2-oxoglutarate aminotransferase (reaction.R00734), 3-sulfino-L-alanine:2-oxoglutarate aminotransferase (reaction.R02619). Component of aspartate aminotransferase (complex.ecocyc.ASPAMINOTRANS-DIMER).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Aspartate aminotransferase (AspAT) (EC 2.6.1.1) (Transaminase A)

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00355|reaction.R00355]] `KEGG` `database` - via EC:2.6.1.1
- `catalyzes` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - via EC:2.6.1.1
- `catalyzes` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - via EC:2.6.1.1
- `catalyzes` --> [[reaction.R02619|reaction.R02619]] `KEGG` `database` - via EC:2.6.1.1
- `is_component_of` --> [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0928|gene.b0928]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00509`
- `KEGG:ecj:JW0911;eco:b0928;ecoc:C3026_05700;`
- `GeneID:93776486;945553;`
- `GO:GO:0004069; GO:0004838; GO:0005737; GO:0005829; GO:0009094; GO:0030170; GO:0033585; GO:0042802; GO:0042803`
- `EC:2.6.1.1`

## Notes

Aspartate aminotransferase (AspAT) (EC 2.6.1.1) (Transaminase A)
