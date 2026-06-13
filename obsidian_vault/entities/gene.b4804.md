---
entity_id: "gene.b4804"
entity_type: "gene"
name: "rbsZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4804"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4804"
  - "rbsZ"
---

# rbsZ

`gene.b4804`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4804`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsZ (gene.b4804) is a gene entity. EcoCyc product frame: RNA0-406. Genomic coordinates: 3937045-3937278.

## Biological Role

Repressed by dsrA (gene.b1954), rbsR (protein.P0ACQ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsZ; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsZ; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17077,GeneID:71004575`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3937045-3937278:+; feature_type=gene
