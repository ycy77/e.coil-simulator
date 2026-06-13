---
entity_id: "gene.b3171"
entity_type: "gene"
name: "metY"
source_database: "NCBI RefSeq"
source_id: "gene-b3171"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3171"
  - "metY"
---

# metY

`gene.b3171`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3171`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metY (gene.b3171) is a gene entity. EcoCyc product frame: metY-tRNA. Genomic coordinates: 3318213-3318289.

## Biological Role

Repressed by argR (protein.P0A6D0), crp (protein.P0ACJ8), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metY; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=metY; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=metY; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=metY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010420,ECOCYC:EG30061,GeneID:947678`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3318213-3318289:-; feature_type=gene
