---
entity_id: "gene.b2073"
entity_type: "gene"
name: "yegL"
source_database: "NCBI RefSeq"
source_id: "gene-b2073"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2073"
  - "yegL"
---

# yegL

`gene.b2073`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2073`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegL (gene.b2073) is a gene entity. It encodes yegL (protein.P76396). Encoded protein function: Uncharacterized protein YegL EcoCyc product frame: G7112-MONOMER. Genomic coordinates: 2152469-2153128. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 16, 2018.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76396|protein.P76396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yegL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006867,ECOCYC:G7112,GeneID:946602`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2152469-2153128:-; feature_type=gene
