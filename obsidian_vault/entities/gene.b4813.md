---
entity_id: "gene.b4813"
entity_type: "gene"
name: "narS"
source_database: "NCBI RefSeq"
source_id: "gene-b4813"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4813"
  - "narS"
---

# narS

`gene.b4813`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4813`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narS (gene.b4813) is a gene entity. EcoCyc product frame: RNA0-416. Genomic coordinates: 1279337-1279520.

## Biological Role

Activated by fnr (protein.P0A9E5), narL (protein.P0AF28).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=narS; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=narS; function=+

## External IDs

- `Dbxref:ECOCYC:G0-17088,GeneID:71004562`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1279337-1279520:+; feature_type=gene
