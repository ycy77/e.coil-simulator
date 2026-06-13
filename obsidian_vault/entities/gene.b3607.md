---
entity_id: "gene.b3607"
entity_type: "gene"
name: "cysE"
source_database: "NCBI RefSeq"
source_id: "gene-b3607"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3607"
  - "cysE"
---

# cysE

`gene.b3607`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3607`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysE (gene.b3607) is a gene entity. It encodes cysE (protein.P0A9D4). Encoded protein function: Serine acetyltransferase (SAT) (EC 2.3.1.30) EcoCyc product frame: SERINE-O-ACETTRAN-MONOMER. Genomic coordinates: 3781741-3782562.

## Biological Role

Repressed by ryhB (gene.b4451), sutR (protein.P77626).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9D4|protein.P0A9D4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=cysE; function=-
- `represses` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=cysE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011793,ECOCYC:EG10187,GeneID:948126`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3781741-3782562:-; feature_type=gene
