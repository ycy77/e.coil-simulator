---
entity_id: "gene.b2682"
entity_type: "gene"
name: "ygaZ"
source_database: "NCBI RefSeq"
source_id: "gene-b2682"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2682"
  - "ygaZ"
---

# ygaZ

`gene.b2682`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2682`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygaZ (gene.b2682) is a gene entity. It encodes ygaZ (protein.P76630). Encoded protein function: Inner membrane protein YgaZ EcoCyc product frame: G7405-MONOMER. Genomic coordinates: 2809617-2810354. EcoCyc protein note: YgaZ is one protein of a putative two-component transporter that is implicated in L-valine export in E. coli K-12. YgaZ has 27% identity to the BrnF protein of the Corynebacterium glutamicum methionine/branched chain amino acid export system . The expression of ygaZ is significantly induced when cells are cultured on mouse cecal mucus compared to cells grown on glucose .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76630|protein.P76630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygaZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008829,ECOCYC:G7405,GeneID:945093`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2809617-2810354:+; feature_type=gene
