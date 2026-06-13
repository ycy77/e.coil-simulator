---
entity_id: "gene.b0498"
entity_type: "gene"
name: "ybbC"
source_database: "NCBI RefSeq"
source_id: "gene-b0498"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0498"
  - "ybbC"
---

# ybbC

`gene.b0498`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0498`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybbC (gene.b0498) is a gene entity. It encodes ybbC (protein.P33668). Encoded protein function: Uncharacterized protein YbbC EcoCyc product frame: EG11769-MONOMER. Genomic coordinates: 527581-527949. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33668|protein.P33668]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybbC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001726,ECOCYC:EG11769,GeneID:945115`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:527581-527949:+; feature_type=gene
