---
entity_id: "gene.b2824"
entity_type: "gene"
name: "ygdB"
source_database: "NCBI RefSeq"
source_id: "gene-b2824"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2824"
  - "ygdB"
---

# ygdB

`gene.b2824`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2824`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygdB (gene.b2824) is a gene entity. It encodes ygdB (protein.P08370). Encoded protein function: Uncharacterized protein YgdB EcoCyc product frame: EG11155-MONOMER. Genomic coordinates: 2962749-2963156.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08370|protein.P08370]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygdB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009261,ECOCYC:EG11155,GeneID:944763`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2962749-2963156:-; feature_type=gene
