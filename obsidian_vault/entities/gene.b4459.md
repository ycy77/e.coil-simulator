---
entity_id: "gene.b4459"
entity_type: "gene"
name: "ryjA"
source_database: "NCBI RefSeq"
source_id: "gene-b4459"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4459"
  - "ryjA"
---

# ryjA

`gene.b4459`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4459`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ryjA (gene.b4459) is a gene entity. EcoCyc product frame: SRAL-RNA. EcoCyc synonyms: psrA24, sraL. Genomic coordinates: 4277926-4278066.

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ryjA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047277,ECOCYC:G0-8875,GeneID:2847753`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4277926-4278066:-; feature_type=gene
