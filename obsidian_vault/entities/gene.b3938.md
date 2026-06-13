---
entity_id: "gene.b3938"
entity_type: "gene"
name: "metJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3938"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3938"
  - "metJ"
---

# metJ

`gene.b3938`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3938`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metJ (gene.b3938) is a gene entity. It encodes metJ (protein.P0A8U6). Encoded protein function: FUNCTION: This regulatory protein, when combined with SAM (S-adenosylmethionine) represses the expression of the methionine regulon and of enzymes involved in SAM synthesis. It is also autoregulated. EcoCyc product frame: PD04032. Genomic coordinates: 4128078-4128395.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8U6|protein.P0A8U6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012874,ECOCYC:EG10588,GeneID:948435`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4128078-4128395:-; feature_type=gene
