---
entity_id: "gene.b3798"
entity_type: "gene"
name: "leuT"
source_database: "NCBI RefSeq"
source_id: "gene-b3798"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3798"
  - "leuT"
---

# leuT

`gene.b3798`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3798`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuT (gene.b3798) is a gene entity. EcoCyc product frame: leuT-tRNA. Genomic coordinates: 3982606-3982692.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=leuT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012403,ECOCYC:EG30049,GeneID:948304`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3982606-3982692:+; feature_type=gene
