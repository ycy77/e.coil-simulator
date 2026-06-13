---
entity_id: "gene.b3797"
entity_type: "gene"
name: "hisR"
source_database: "NCBI RefSeq"
source_id: "gene-b3797"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3797"
  - "hisR"
---

# hisR

`gene.b3797`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3797`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisR (gene.b3797) is a gene entity. EcoCyc product frame: hisR-tRNA. EcoCyc synonyms: hisT. Genomic coordinates: 3982509-3982585.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hisR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012401,ECOCYC:EG30042,GeneID:948305`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3982509-3982585:+; feature_type=gene
