---
entity_id: "gene.b1571"
entity_type: "gene"
name: "ydfA"
source_database: "NCBI RefSeq"
source_id: "gene-b1571"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1571"
  - "ydfA"
---

# ydfA

`gene.b1571`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1571`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfA (gene.b1571) is a gene entity. It encodes ydfA (protein.P0ACW8). Encoded protein function: Uncharacterized protein YdfA EcoCyc product frame: EG11300-MONOMER. Genomic coordinates: 1648508-1648663. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 8, 2017.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACW8|protein.P0ACW8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydfA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005251,ECOCYC:EG11300,GeneID:946082`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1648508-1648663:+; feature_type=gene
