---
entity_id: "gene.b0122"
entity_type: "gene"
name: "yacC"
source_database: "NCBI RefSeq"
source_id: "gene-b0122"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0122"
  - "yacC"
---

# yacC

`gene.b0122`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0122`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yacC (gene.b0122) is a gene entity. It encodes yacC (protein.P0AA95). Encoded protein function: Uncharacterized protein YacC EcoCyc product frame: EG11089-MONOMER. Genomic coordinates: 136570-136917. EcoCyc protein note: yacC is cotranscribed with speED . A deletion upstream of speE, extending into the yacC open reading frame, leads to loss of spermidine synthase and S-adenosylmethionine decarboxylase activity .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA95|protein.P0AA95]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yacC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000423,ECOCYC:EG11089,GeneID:948472`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:136570-136917:-; feature_type=gene
