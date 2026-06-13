---
entity_id: "gene.b4402"
entity_type: "gene"
name: "yjjY"
source_database: "NCBI RefSeq"
source_id: "gene-b4402"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4402"
  - "yjjY"
---

# yjjY

`gene.b4402`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4402`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjjY (gene.b4402) is a gene entity. It encodes yjjY (protein.P0ADD9). Encoded protein function: Uncharacterized protein YjjY EcoCyc product frame: G7954-MONOMER. Genomic coordinates: 4640402-4640542. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 12, 2020.

## Biological Role

Activated by zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADD9|protein.P0ADD9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=yjjY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014437,ECOCYC:G7954,GeneID:948925`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4640402-4640542:+; feature_type=gene
