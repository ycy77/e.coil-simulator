---
entity_id: "gene.b4625"
entity_type: "gene"
name: "symR"
source_database: "NCBI RefSeq"
source_id: "gene-b4625"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4625"
  - "symR"
---

# symR

`gene.b4625`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4625`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

symR (gene.b4625) is a gene entity. EcoCyc product frame: RNA0-334. EcoCyc synonyms: ryjC. Genomic coordinates: 4579835-4579911.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=symR; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10610,GeneID:5061533`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4579835-4579911:+; feature_type=gene
