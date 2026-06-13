---
entity_id: "gene.b3027"
entity_type: "gene"
name: "ygiZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3027"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3027"
  - "ygiZ"
---

# ygiZ

`gene.b3027`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3027`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiZ (gene.b3027) is a gene entity. It encodes ygiZ (protein.Q46867). Encoded protein function: Inner membrane protein YgiZ EcoCyc product frame: G7577-MONOMER. Genomic coordinates: 3171879-3172211. EcoCyc protein note: YgiZ is an inner membrane protein with three predicted transmembrane domains. The C terminus is located in the periplasm . Expression of ygiZ is activated by BglJ-RcsB .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46867|protein.Q46867]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygiZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009940,ECOCYC:G7577,GeneID:946450`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3171879-3172211:-; feature_type=gene
