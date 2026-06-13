---
entity_id: "gene.b1555"
entity_type: "gene"
name: "ydfR"
source_database: "NCBI RefSeq"
source_id: "gene-b1555"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1555"
  - "ydfR"
---

# ydfR

`gene.b1555`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1555`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfR (gene.b1555) is a gene entity. It encodes ydfR (protein.P76160). Encoded protein function: Uncharacterized protein YdfR EcoCyc product frame: G6828-MONOMER. Genomic coordinates: 1640054-1640365. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 5, 2006.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76160|protein.P76160]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydfR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005192,ECOCYC:G6828,GeneID:946095`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1640054-1640365:-; feature_type=gene
