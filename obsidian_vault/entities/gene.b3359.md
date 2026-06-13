---
entity_id: "gene.b3359"
entity_type: "gene"
name: "argD"
source_database: "NCBI RefSeq"
source_id: "gene-b3359"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3359"
  - "argD"
---

# argD

`gene.b3359`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3359`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argD (gene.b3359) is a gene entity. It encodes argD (protein.P18335). Encoded protein function: FUNCTION: Involved in both the arginine and lysine biosynthetic pathways. {ECO:0000255|HAMAP-Rule:MF_01107, ECO:0000269|PubMed:10074354}. EcoCyc product frame: ACETYLORNTRANSAM-MONOMER. EcoCyc synonyms: Arg1, dapC, dtu. Genomic coordinates: 3488960-3490180.

## Biological Role

Repressed by argR (protein.P0A6D0).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18335|protein.P18335]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=argD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010976,ECOCYC:EG10066,GeneID:947864`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3488960-3490180:-; feature_type=gene
