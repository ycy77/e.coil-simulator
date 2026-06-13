---
entity_id: "gene.b2497"
entity_type: "gene"
name: "uraA"
source_database: "NCBI RefSeq"
source_id: "gene-b2497"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2497"
  - "uraA"
---

# uraA

`gene.b2497`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2497`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uraA (gene.b2497) is a gene entity. It encodes uraA (protein.P0AGM7). Encoded protein function: FUNCTION: Transport of uracil in the cell. {ECO:0000269|PubMed:21423164, ECO:0000269|PubMed:7721693}. EcoCyc product frame: URAA-MONOMER. Genomic coordinates: 2618871-2620160.

## Biological Role

Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGM7|protein.P0AGM7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uraA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=uraA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008219,ECOCYC:EG12129,GeneID:946978`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2618871-2620160:-; feature_type=gene
