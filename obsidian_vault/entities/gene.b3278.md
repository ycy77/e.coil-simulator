---
entity_id: "gene.b3278"
entity_type: "gene"
name: "rrsD"
source_database: "NCBI RefSeq"
source_id: "gene-b3278"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3278"
  - "rrsD"
---

# rrsD

`gene.b3278`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3278`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrsD (gene.b3278) is a gene entity. EcoCyc product frame: RRSD-RRNA. Genomic coordinates: 3427221-3428762.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrsD; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrsD; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrsD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010753,ECOCYC:EG30087,GeneID:947777`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:3427221-3428762:-; feature_type=gene
