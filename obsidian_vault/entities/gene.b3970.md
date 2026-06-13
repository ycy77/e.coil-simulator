---
entity_id: "gene.b3970"
entity_type: "gene"
name: "rrlB"
source_database: "NCBI RefSeq"
source_id: "gene-b3970"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3970"
  - "rrlB"
---

# rrlB

`gene.b3970`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3970`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlB (gene.b3970) is a gene entity. EcoCyc product frame: RRLB-RRNA. Genomic coordinates: 4168641-4171544.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrlB; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrlB; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrlB; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=rrlB; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=rrlB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012995,ECOCYC:EG30078,GeneID:948473`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:4168641-4171544:+; feature_type=gene
