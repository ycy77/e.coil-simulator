---
entity_id: "gene.b0888"
entity_type: "gene"
name: "trxB"
source_database: "NCBI RefSeq"
source_id: "gene-b0888"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0888"
  - "trxB"
---

# trxB

`gene.b0888`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0888`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trxB (gene.b0888) is a gene entity. It encodes trxB (protein.P0A9P4). Encoded protein function: Thioredoxin reductase (TRXR) (EC 1.8.1.9) EcoCyc product frame: THIOREDOXIN-REDUCT-NADPH-MONOMER. EcoCyc synonyms: trxR. Genomic coordinates: 931085-932050.

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9P4|protein.P0A9P4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=trxB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003018,ECOCYC:EG11032,GeneID:949054`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:931085-932050:-; feature_type=gene
