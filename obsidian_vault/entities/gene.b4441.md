---
entity_id: "gene.b4441"
entity_type: "gene"
name: "glmY"
source_database: "NCBI RefSeq"
source_id: "gene-b4441"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4441"
  - "glmY"
---

# glmY

`gene.b4441`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4441`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glmY (gene.b4441) is a gene entity. EcoCyc product frame: TKE1-RNA. EcoCyc synonyms: tke1, sroF. Genomic coordinates: 2691157-2691340.

## Biological Role

Activated by rpoD (protein.P00579), glrR (protein.P0AFU4), rpoN (protein.P24255).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glmY; function=+
- `activates` <-- [[protein.P0AFU4|protein.P0AFU4]] `RegulonDB` `C` - regulator=GlrR; target=glmY; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=glmY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047261,ECOCYC:G0-8910,GeneID:2847700`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2691157-2691340:-; feature_type=gene
