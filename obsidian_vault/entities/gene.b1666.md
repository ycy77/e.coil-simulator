---
entity_id: "gene.b1666"
entity_type: "gene"
name: "valW"
source_database: "NCBI RefSeq"
source_id: "gene-b1666"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1666"
  - "valW"
---

# valW

`gene.b1666`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1666`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

valW (gene.b1666) is a gene entity. EcoCyc product frame: valW-tRNA. Genomic coordinates: 1746516-1746592.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=valW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005569,ECOCYC:EG30112,GeneID:949069`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:1746516-1746592:+; feature_type=gene
