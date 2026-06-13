---
entity_id: "gene.b4517"
entity_type: "gene"
name: "gnsA"
source_database: "NCBI RefSeq"
source_id: "gene-b4517"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4517"
  - "gnsA"
---

# gnsA

`gene.b4517`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4517`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gnsA (gene.b4517) is a gene entity. It encodes gnsA (protein.P0AC92). Encoded protein function: FUNCTION: Overexpression increases levels of unsaturated fatty acids and suppresses both the temperature-sensitive fabA6 mutation and cold-sensitive secG null mutation. {ECO:0000269|PubMed:11544213}. EcoCyc product frame: MONOMER0-1701. EcoCyc synonyms: yccL, sfa. Genomic coordinates: 1052067-1052240.

## Biological Role

Activated by rpoD (protein.P00579), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC92|protein.P0AC92]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gnsA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=gnsA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285038,ECOCYC:G0-9662,GeneID:1450249`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1052067-1052240:+; feature_type=gene
