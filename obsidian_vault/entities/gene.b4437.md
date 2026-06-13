---
entity_id: "gene.b4437"
entity_type: "gene"
name: "sibB"
source_database: "NCBI RefSeq"
source_id: "gene-b4437"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4437"
  - "sibB"
---

# sibB

`gene.b4437`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4437`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sibB (gene.b4437) is a gene entity. EcoCyc product frame: RYED-RNA. EcoCyc synonyms: QUAD1b, tpe60, ryeD. Genomic coordinates: 2153646-2153781.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sibB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047257,ECOCYC:G0-8885,GeneID:2847674`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2153646-2153781:+; feature_type=gene
