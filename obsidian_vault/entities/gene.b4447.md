---
entity_id: "gene.b4447"
entity_type: "gene"
name: "sibD"
source_database: "NCBI RefSeq"
source_id: "gene-b4447"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4447"
  - "sibD"
---

# sibD

`gene.b4447`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4447`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sibD (gene.b4447) is a gene entity. EcoCyc product frame: C0730-RNA. EcoCyc synonyms: tp8, C0730, IS156, QUAD1d, rygD. Genomic coordinates: 3194721-3194865.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sibD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047267,ECOCYC:G0-8913,GeneID:2847684`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3194721-3194865:-; feature_type=gene
