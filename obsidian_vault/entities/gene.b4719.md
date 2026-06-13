---
entity_id: "gene.b4719"
entity_type: "gene"
name: "sdsN"
source_database: "NCBI RefSeq"
source_id: "gene-b4719"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4719"
  - "sdsN"
---

# sdsN

`gene.b4719`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4719`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdsN (gene.b4719) is a gene entity. EcoCyc product frame: RNA0-361. Genomic coordinates: 1996921-1997057.

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (3)

- `represses` --> [[gene.b0851|gene.b0851]] `RegulonDB` `S` - regulator=SdsN; target=nfsA; function=-
- `represses` --> [[gene.b2193|gene.b2193]] `RegulonDB` `S` - regulator=SdsN; target=narP; function=-
- `represses` --> [[gene.b2552|gene.b2552]] `RegulonDB` `S` - regulator=SdsN; target=hmp; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sdsN; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10699,GeneID:38094968`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1996921-1997057:+; feature_type=gene
