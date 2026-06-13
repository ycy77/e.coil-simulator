---
entity_id: "gene.b4717"
entity_type: "gene"
name: "micL"
source_database: "NCBI RefSeq"
source_id: "gene-b4717"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4717"
  - "micL"
---

# micL

`gene.b4717`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4717`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

micL (gene.b4717) is a gene entity. EcoCyc product frame: RNA0-386. EcoCyc synonyms: slrA, ryeF. Genomic coordinates: 1958441-1958747.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b1677|gene.b1677]] `RegulonDB` `S` - regulator=MicL; target=lpp; function=-

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=micL; function=+

## External IDs

- `Dbxref:ECOCYC:G0-16601,GeneID:38094966`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1958441-1958747:-; feature_type=gene
