---
entity_id: "gene.b1665"
entity_type: "gene"
name: "valV"
source_database: "NCBI RefSeq"
source_id: "gene-b1665"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1665"
  - "valV"
---

# valV

`gene.b1665`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1665`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

valV (gene.b1665) is a gene entity. EcoCyc product frame: valV-tRNA. Genomic coordinates: 1746435-1746511.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=valV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005567,ECOCYC:EG30111,GeneID:946170`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:1746435-1746511:+; feature_type=gene
