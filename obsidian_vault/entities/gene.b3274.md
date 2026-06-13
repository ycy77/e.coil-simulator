---
entity_id: "gene.b3274"
entity_type: "gene"
name: "rrfD"
source_database: "NCBI RefSeq"
source_id: "gene-b3274"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3274"
  - "rrfD"
---

# rrfD

`gene.b3274`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3274`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfD (gene.b3274) is a gene entity. EcoCyc product frame: RRFD-RRNA. Genomic coordinates: 3423668-3423787.

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrfD; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfD; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrfD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010744,ECOCYC:EG30073,GeneID:947769`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3423668-3423787:-; feature_type=gene
