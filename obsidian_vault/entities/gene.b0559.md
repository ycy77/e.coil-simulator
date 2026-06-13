---
entity_id: "gene.b0559"
entity_type: "gene"
name: "ybcW"
source_database: "NCBI RefSeq"
source_id: "gene-b0559"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0559"
  - "ybcW"
---

# ybcW

`gene.b0559`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0559`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybcW (gene.b0559) is a gene entity. It encodes ybcW (protein.P64435). Encoded protein function: Uncharacterized protein YbcW EcoCyc product frame: G6314-MONOMER. Genomic coordinates: 579880-580086. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 20, 2018.

## Biological Role

Activated by pdhR (protein.P0ACL9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64435|protein.P64435]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=ybcW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001912,ECOCYC:G6314,GeneID:945175`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:579880-580086:+; feature_type=gene
