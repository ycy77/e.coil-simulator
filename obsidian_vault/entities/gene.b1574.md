---
entity_id: "gene.b1574"
entity_type: "gene"
name: "dicF"
source_database: "NCBI RefSeq"
source_id: "gene-b1574"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1574"
  - "dicF"
---

# dicF

`gene.b1574`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1574`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dicF (gene.b1574) is a gene entity. EcoCyc product frame: DICF-RNA. Genomic coordinates: 1649382-1649434.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (4)

- `represses` --> [[gene.b0095|gene.b0095]] `RegulonDB` `S` - regulator=DicF; target=ftsZ; function=-
- `represses` --> [[gene.b1817|gene.b1817]] `RegulonDB` `S` - regulator=DicF; target=manX; function=-
- `represses` --> [[gene.b1854|gene.b1854]] `RegulonDB` `S` - regulator=DicF; target=pykA; function=-
- `represses` --> [[gene.b3569|gene.b3569]] `RegulonDB` `S` - regulator=DicF; target=xylR; function=-

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005257,ECOCYC:EG31115,GeneID:946140`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1649382-1649434:+; feature_type=gene
