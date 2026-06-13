---
entity_id: "gene.b2143"
entity_type: "gene"
name: "cdd"
source_database: "NCBI RefSeq"
source_id: "gene-b2143"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2143"
  - "cdd"
---

# cdd

`gene.b2143`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2143`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cdd (gene.b2143) is a gene entity. It encodes cdd (protein.P0ABF6). Encoded protein function: FUNCTION: This enzyme scavenges exogenous and endogenous cytidine and 2'-deoxycytidine for UMP synthesis. EcoCyc product frame: CYTIDEAM-MONOMER. Genomic coordinates: 2231844-2232728.

## Biological Role

Repressed by crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABF6|protein.P0ABF6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cdd; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cdd; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cdd; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=cdd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007086,ECOCYC:EG10137,GeneID:946663`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2231844-2232728:+; feature_type=gene
