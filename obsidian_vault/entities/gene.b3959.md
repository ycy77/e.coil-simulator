---
entity_id: "gene.b3959"
entity_type: "gene"
name: "argB"
source_database: "NCBI RefSeq"
source_id: "gene-b3959"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3959"
  - "argB"
---

# argB

`gene.b3959`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3959`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argB (gene.b3959) is a gene entity. It encodes argB (protein.P0A6C8). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of N-acetyl-L-glutamate. {ECO:0000255|HAMAP-Rule:MF_00082, ECO:0000269|PubMed:10393305, ECO:0000269|PubMed:14623187}. EcoCyc product frame: ACETYLGLUTKIN-MONOMER. Genomic coordinates: 4156013-4156789.

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6C8|protein.P0A6C8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argB; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012967,ECOCYC:EG10064,GeneID:948464`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4156013-4156789:+; feature_type=gene
