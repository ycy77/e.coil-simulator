---
entity_id: "gene.b4013"
entity_type: "gene"
name: "metA"
source_database: "NCBI RefSeq"
source_id: "gene-b4013"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4013"
  - "metA"
---

# metA

`gene.b4013`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4013`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metA (gene.b4013) is a gene entity. It encodes metAS (protein.P07623). Encoded protein function: FUNCTION: Transfers a succinyl group from succinyl-CoA to L-homoserine, forming succinyl-L-homoserine (PubMed:10572016, PubMed:17302437, PubMed:17442255, PubMed:28581482). Utilizes a ping-pong kinetic mechanism in which the succinyl group of succinyl-CoA is initially transferred to the enzyme to form a succinyl-enzyme intermediate before subsequent transfer to homoserine to form the final product, O-succinylhomoserine (PubMed:10572016, PubMed:17302437, PubMed:17442255). Cannot use acetyl-CoA (PubMed:10572016). {ECO:0000269|PubMed:10572016, ECO:0000269|PubMed:17302437, ECO:0000269|PubMed:17442255, ECO:0000269|PubMed:28581482}. EcoCyc product frame: HOMSUCTRAN-MONOMER. Genomic coordinates: 4214280-4215209.

## Biological Role

Repressed by metJ (protein.P0A8U6). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07623|protein.P07623]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=metA; function=+
- `represses` <-- [[protein.P0A8U6|protein.P0A8U6]] `RegulonDB` `C` - regulator=MetJ; target=metA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013121,ECOCYC:EG10581,GeneID:948513`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4214280-4215209:+; feature_type=gene
