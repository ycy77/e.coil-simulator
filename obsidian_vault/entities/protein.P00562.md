---
entity_id: "protein.P00562"
entity_type: "protein"
name: "metL"
source_database: "UniProt"
source_id: "P00562"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metL metM b3940 JW3911"
---

# metL

`protein.P00562`

## Static

- Type: `protein`
- Source: `UniProt:P00562`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Bifunctional aspartate kinase and homoserine dehydrogenase that catalyzes the first and the third steps toward the synthesis of lysine, methionine and threonine from aspartate. {ECO:0000250|UniProtKB:Q9SA18}.

## Biological Role

Catalyzes ATP:L-aspartate 4-phosphotransferase (reaction.R00480). Component of fused aspartate kinase/homoserine dehydrogenase 2 (complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Bifunctional aspartate kinase and homoserine dehydrogenase that catalyzes the first and the third steps toward the synthesis of lysine, methionine and threonine from aspartate. {ECO:0000250|UniProtKB:Q9SA18}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00480|reaction.R00480]] `KEGG` `database` - via EC:2.7.2.4
- `is_component_of` --> [[complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX|complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3940|gene.b3940]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00562`
- `KEGG:ecj:JW3911;eco:b3940;ecoc:C3026_21290;`
- `GeneID:86861662;948433;`
- `GO:GO:0004072; GO:0004412; GO:0005524; GO:0005829; GO:0009086; GO:0009088; GO:0009089; GO:0009090; GO:0046872; GO:0050661; GO:0070403`
- `EC:1.1.1.3; 2.7.2.4`

## Notes

Bifunctional aspartokinase/homoserine dehydrogenase 2 (Aspartokinase II/homoserine dehydrogenase II) (AKII-HDII) [Includes: Aspartokinase (EC 2.7.2.4); Homoserine dehydrogenase (EC 1.1.1.3)]
