---
entity_id: "gene.b4838"
entity_type: "gene"
name: "fimR2"
source_database: "NCBI RefSeq"
source_id: "gene-b4838"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4838"
  - "fimR2"
---

# fimR2

`gene.b4838`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4838`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimR2 (gene.b4838) is a gene entity. EcoCyc product frame: RNA0-432. Genomic coordinates: 4543674-4543708.

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimR2; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimR2; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimR2; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimR2; function=+

## External IDs

- `Dbxref:ECOCYC:G0-17115,GeneID:302211672`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4543674-4543708:+; feature_type=gene
