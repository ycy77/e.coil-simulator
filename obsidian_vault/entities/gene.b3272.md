---
entity_id: "gene.b3272"
entity_type: "gene"
name: "rrfF"
source_database: "NCBI RefSeq"
source_id: "gene-b3272"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3272"
  - "rrfF"
---

# rrfF

`gene.b3272`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3272`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfF (gene.b3272) is a gene entity. EcoCyc product frame: RRFF-RRNA. EcoCyc synonyms: rrfDbeta, rrvD. Genomic coordinates: 3423423-3423542.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrfF; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrfF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010740,ECOCYC:EG30091,GeneID:947771`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3423423-3423542:-; feature_type=gene
