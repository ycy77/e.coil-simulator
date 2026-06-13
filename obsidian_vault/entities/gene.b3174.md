---
entity_id: "gene.b3174"
entity_type: "gene"
name: "leuU"
source_database: "NCBI RefSeq"
source_id: "gene-b3174"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3174"
  - "leuU"
---

# leuU

`gene.b3174`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3174`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuU (gene.b3174) is a gene entity. EcoCyc product frame: leuU-tRNA. Genomic coordinates: 3322072-3322158.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuU; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=leuU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010434,ECOCYC:EG30050,GeneID:947505`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3322072-3322158:-; feature_type=gene
