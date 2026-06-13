---
entity_id: "gene.b3648"
entity_type: "gene"
name: "gmk"
source_database: "NCBI RefSeq"
source_id: "gene-b3648"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3648"
  - "gmk"
---

# gmk

`gene.b3648`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3648`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gmk (gene.b3648) is a gene entity. It encodes gmk (protein.P60546). Encoded protein function: FUNCTION: Essential for recycling GMP and indirectly, cGMP. {ECO:0000269|PubMed:8390989}. EcoCyc product frame: GUANYL-KIN-MONOMER. EcoCyc synonyms: spoR. Genomic coordinates: 3821428-3822051.

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60546|protein.P60546]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gmk; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011930,ECOCYC:EG10965,GeneID:948163`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3821428-3822051:+; feature_type=gene
