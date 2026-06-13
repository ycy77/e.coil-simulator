---
entity_id: "gene.b3971"
entity_type: "gene"
name: "rrfB"
source_database: "NCBI RefSeq"
source_id: "gene-b3971"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3971"
  - "rrfB"
---

# rrfB

`gene.b3971`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3971`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfB (gene.b3971) is a gene entity. EcoCyc product frame: RRFB-RRNA. Genomic coordinates: 4171637-4171756.

## Biological Role

Repressed by hns (protein.P0ACF8), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrfB; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfB; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrfB; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=rrfB; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrfB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012997,ECOCYC:EG30071,GeneID:948471`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4171637-4171756:+; feature_type=gene
