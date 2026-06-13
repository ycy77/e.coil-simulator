---
entity_id: "gene.b2985"
entity_type: "gene"
name: "yghS"
source_database: "NCBI RefSeq"
source_id: "gene-b2985"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2985"
  - "yghS"
---

# yghS

`gene.b2985`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2985`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghS (gene.b2985) is a gene entity. It encodes yghS (protein.Q46843). Encoded protein function: Uncharacterized ATP-binding protein YghS EcoCyc product frame: G7551-MONOMER. Genomic coordinates: 3133244-3133957. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 20, 2017.

## Biological Role

Repressed by leuO (protein.P10151), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46843|protein.Q46843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=yghS; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yghS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009793,ECOCYC:G7551,GeneID:947476`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3133244-3133957:-; feature_type=gene
