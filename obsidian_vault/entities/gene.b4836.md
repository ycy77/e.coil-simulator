---
entity_id: "gene.b4836"
entity_type: "gene"
name: "glnZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4836"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4836"
  - "glnZ"
---

# glnZ

`gene.b4836`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4836`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnZ (gene.b4836) is a gene entity. EcoCyc product frame: RNA0-434. Genomic coordinates: 4056428-4056621.

## Biological Role

Repressed by glnG (protein.P0AFB8). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), glnG (protein.P0AFB8), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (2)

- `represses` --> [[gene.b0726|gene.b0726]] `RegulonDB` `S` - regulator=GlnZ; target=sucA; function=-
- `represses` --> [[gene.b0810|gene.b0810]] `RegulonDB` `S` - regulator=GlnZ; target=glnP; function=-

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glnZ; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=glnZ; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `C` - regulator=NtrC; target=glnZ; function=-+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=glnZ; function=+
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `C` - regulator=NtrC; target=glnZ; function=-+

## External IDs

- `Dbxref:ECOCYC:G0-17117,GeneID:302211669`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4056428-4056621:-; feature_type=gene
