---
entity_id: "gene.b3799"
entity_type: "gene"
name: "proM"
source_database: "NCBI RefSeq"
source_id: "gene-b3799"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3799"
  - "proM"
---

# proM

`gene.b3799`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3799`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proM (gene.b3799) is a gene entity. EcoCyc product frame: proM-tRNA. EcoCyc synonyms: proU. Genomic coordinates: 3982735-3982811.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=proM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012405,ECOCYC:EG30068,GeneID:948303`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3982735-3982811:+; feature_type=gene
