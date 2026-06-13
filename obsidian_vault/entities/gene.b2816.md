---
entity_id: "gene.b2816"
entity_type: "gene"
name: "metV"
source_database: "NCBI RefSeq"
source_id: "gene-b2816"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2816"
  - "metV"
---

# metV

`gene.b2816`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2816`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metV (gene.b2816) is a gene entity. EcoCyc product frame: RNA0-306. EcoCyc synonyms: metZbeta, metX, metZ-β, metZb. Genomic coordinates: 2947607-2947683.

## Biological Role

Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=metV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009236,ECOCYC:EG30060,GeneID:946037`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2947607-2947683:+; feature_type=gene
