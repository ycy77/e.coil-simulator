---
entity_id: "gene.b1573"
entity_type: "gene"
name: "ydfC"
source_database: "NCBI RefSeq"
source_id: "gene-b1573"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1573"
  - "ydfC"
---

# ydfC

`gene.b1573`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1573`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfC (gene.b1573) is a gene entity. It encodes ydfC (protein.P21418). Encoded protein function: Uncharacterized protein YdfC EcoCyc product frame: EG11302-MONOMER. Genomic coordinates: 1648823-1649041. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 10, 2017.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21418|protein.P21418]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydfC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005255,ECOCYC:EG11302,GeneID:946107`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1648823-1649041:+; feature_type=gene
