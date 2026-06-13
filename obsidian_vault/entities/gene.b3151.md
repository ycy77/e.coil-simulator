---
entity_id: "gene.b3151"
entity_type: "gene"
name: "yraQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3151"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3151"
  - "yraQ"
---

# yraQ

`gene.b3151`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3151`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yraQ (gene.b3151) is a gene entity. It encodes yraQ (protein.P45468). Encoded protein function: UPF0718 protein YraQ EcoCyc product frame: G7645-MONOMER. Genomic coordinates: 3297098-3298138. EcoCyc protein note: No information about this protein was found by a literature search conducted on January 30, 2014.

## Biological Role

Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45468|protein.P45468]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=yraQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010353,ECOCYC:G7645,GeneID:947668`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3297098-3298138:-; feature_type=gene
