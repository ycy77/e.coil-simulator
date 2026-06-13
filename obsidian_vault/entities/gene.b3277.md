---
entity_id: "gene.b3277"
entity_type: "gene"
name: "ileU"
source_database: "NCBI RefSeq"
source_id: "gene-b3277"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3277"
  - "ileU"
---

# ileU

`gene.b3277`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3277`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ileU (gene.b3277) is a gene entity. EcoCyc product frame: ileU-tRNA. EcoCyc synonyms: tilD. Genomic coordinates: 3427076-3427152.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ileU; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ileU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010750,ECOCYC:EG30044,GeneID:947778`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3427076-3427152:-; feature_type=gene
