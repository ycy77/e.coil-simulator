---
entity_id: "protein.P07623"
entity_type: "protein"
name: "metAS"
source_database: "UniProt"
source_id: "P07623"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00295, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metAS metA b4013 JW3973"
---

# metAS

`protein.P07623`

## Static

- Type: `protein`
- Source: `UniProt:P07623`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00295, ECO:0000305}.

## Enriched Summary

FUNCTION: Transfers a succinyl group from succinyl-CoA to L-homoserine, forming succinyl-L-homoserine (PubMed:10572016, PubMed:17302437, PubMed:17442255, PubMed:28581482). Utilizes a ping-pong kinetic mechanism in which the succinyl group of succinyl-CoA is initially transferred to the enzyme to form a succinyl-enzyme intermediate before subsequent transfer to homoserine to form the final product, O-succinylhomoserine (PubMed:10572016, PubMed:17302437, PubMed:17442255). Cannot use acetyl-CoA (PubMed:10572016). {ECO:0000269|PubMed:10572016, ECO:0000269|PubMed:17302437, ECO:0000269|PubMed:17442255, ECO:0000269|PubMed:28581482}.

## Biological Role

Component of homoserine O-succinyltransferase (complex.ecocyc.HOMSUCTRAN-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Transfers a succinyl group from succinyl-CoA to L-homoserine, forming succinyl-L-homoserine (PubMed:10572016, PubMed:17302437, PubMed:17442255, PubMed:28581482). Utilizes a ping-pong kinetic mechanism in which the succinyl group of succinyl-CoA is initially transferred to the enzyme to form a succinyl-enzyme intermediate before subsequent transfer to homoserine to form the final product, O-succinylhomoserine (PubMed:10572016, PubMed:17302437, PubMed:17442255). Cannot use acetyl-CoA (PubMed:10572016). {ECO:0000269|PubMed:10572016, ECO:0000269|PubMed:17302437, ECO:0000269|PubMed:17442255, ECO:0000269|PubMed:28581482}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HOMSUCTRAN-CPLX|complex.ecocyc.HOMSUCTRAN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4013|gene.b4013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07623`
- `KEGG:ecj:JW3973;eco:b4013;ecoc:C3026_21680;`
- `GeneID:948513;`
- `GO:GO:0004414; GO:0005737; GO:0008899; GO:0019281; GO:0042803`
- `EC:2.3.1.46`

## Notes

Homoserine O-succinyltransferase (HST) (EC 2.3.1.46) (Homoserine transsuccinylase) (HTS)
