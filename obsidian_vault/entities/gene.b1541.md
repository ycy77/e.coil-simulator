---
entity_id: "gene.b1541"
entity_type: "gene"
name: "ydfZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1541"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1541"
  - "ydfZ"
---

# ydfZ

`gene.b1541`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1541`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfZ (gene.b1541) is a gene entity. It encodes ydfZ (protein.P64463). Encoded protein function: Putative selenoprotein YdfZ EcoCyc product frame: G6815-MONOMER. Genomic coordinates: 1629215-1629418. EcoCyc protein note: An oxidized proteoform of YdfZ was found to be significantly more abundant when grown in glucose as compared to acetate based on a new quantitative top-down proteomics method using iodo-tandem mass tags .

## Biological Role

Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64463|protein.P64463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ydfZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005147,ECOCYC:G6815,GeneID:948796`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1629215-1629418:+; feature_type=gene
