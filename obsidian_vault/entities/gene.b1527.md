---
entity_id: "gene.b1527"
entity_type: "gene"
name: "yneK"
source_database: "NCBI RefSeq"
source_id: "gene-b1527"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1527"
  - "yneK"
---

# yneK

`gene.b1527`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1527`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yneK (gene.b1527) is a gene entity. It encodes yneK (protein.P76150). Encoded protein function: Uncharacterized protein YneK EcoCyc product frame: G6813-MONOMER. Genomic coordinates: 1615763-1616878. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 9, 2008.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76150|protein.P76150]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yneK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005100,ECOCYC:G6813,GeneID:946080`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1615763-1616878:+; feature_type=gene
