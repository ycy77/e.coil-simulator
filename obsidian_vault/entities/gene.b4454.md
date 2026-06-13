---
entity_id: "gene.b4454"
entity_type: "gene"
name: "rdlD"
source_database: "NCBI RefSeq"
source_id: "gene-b4454"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4454"
  - "rdlD"
---

# rdlD

`gene.b4454`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4454`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rdlD (gene.b4454) is a gene entity. EcoCyc product frame: RDLD-RNA. Genomic coordinates: 3700136-3700199.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rdlD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047273,ECOCYC:G0-9042,GeneID:2847731`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3700136-3700199:+; feature_type=gene
