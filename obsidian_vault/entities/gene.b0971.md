---
entity_id: "gene.b0971"
entity_type: "gene"
name: "serT"
source_database: "NCBI RefSeq"
source_id: "gene-b0971"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0971"
  - "serT"
---

# serT

`gene.b0971`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0971`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

serT (gene.b0971) is a gene entity. EcoCyc product frame: serT-tRNA. EcoCyc synonyms: divE. Genomic coordinates: 1031625-1031712.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=serT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003283,ECOCYC:EG30093,GeneID:944826`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:1031625-1031712:-; feature_type=gene
