---
entity_id: "gene.b4624"
entity_type: "gene"
name: "ryjB"
source_database: "NCBI RefSeq"
source_id: "gene-b4624"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4624"
  - "ryjB"
---

# ryjB

`gene.b4624`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4624`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ryjB (gene.b4624) is a gene entity. EcoCyc product frame: RNA0-333. Genomic coordinates: 4527977-4528066.

## Biological Role

Activated by rpoD (protein.P00579), phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ryjB; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-10609,GeneID:5061532`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4527977-4528066:+; feature_type=gene
