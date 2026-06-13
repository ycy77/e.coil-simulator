---
entity_id: "gene.b4414"
entity_type: "gene"
name: "tff"
source_database: "NCBI RefSeq"
source_id: "gene-b4414"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4414"
  - "tff"
---

# tff

`gene.b4414`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4414`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tff (gene.b4414) is a gene entity. EcoCyc product frame: T44-RNA. EcoCyc synonyms: t44. Genomic coordinates: 189712-189847.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tff; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tff; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0047239,ECOCYC:G0-8895,GeneID:2847773`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:189712-189847:+; feature_type=gene
