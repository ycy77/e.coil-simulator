---
entity_id: "gene.b2591"
entity_type: "gene"
name: "rrsG"
source_database: "NCBI RefSeq"
source_id: "gene-b2591"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2591"
  - "rrsG"
---

# rrsG

`gene.b2591`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2591`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrsG (gene.b2591) is a gene entity. EcoCyc product frame: RRSG-RRNA. Genomic coordinates: 2729616-2731157.

## Biological Role

Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrsG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008525,ECOCYC:EG30089,GeneID:947071`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:2729616-2731157:-; feature_type=gene
