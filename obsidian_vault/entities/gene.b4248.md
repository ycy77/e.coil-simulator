---
entity_id: "gene.b4248"
entity_type: "gene"
name: "yjgH"
source_database: "NCBI RefSeq"
source_id: "gene-b4248"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4248"
  - "yjgH"
---

# yjgH

`gene.b4248`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4248`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjgH (gene.b4248) is a gene entity. It encodes yjgH (protein.P39332). Encoded protein function: RutC family protein YjgH EcoCyc product frame: G7879-MONOMER. Genomic coordinates: 4472814-4473209. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 8, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39332|protein.P39332]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjgH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013905,ECOCYC:G7879,GeneID:948769`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4472814-4473209:-; feature_type=gene
