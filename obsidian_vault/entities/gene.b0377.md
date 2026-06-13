---
entity_id: "gene.b0377"
entity_type: "gene"
name: "sbmA"
source_database: "NCBI RefSeq"
source_id: "gene-b0377"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0377"
  - "sbmA"
---

# sbmA

`gene.b0377`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0377`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sbmA (gene.b0377) is a gene entity. It encodes sbmA (protein.P0AFY6). Encoded protein function: FUNCTION: Uptake of antimicrobial peptides. Required for the transport of microcin B17 (MccB17), microcin 25 (Mcc25) and proline-rich antimicrobial peptides (such as Cathelicidin-3, Arasin 1 and Dro/Drosocin) into the cell. {ECO:0000269|PubMed:17725560, ECO:0000269|PubMed:3543211, ECO:0000269|PubMed:36997646, ECO:0000269|PubMed:7768835, ECO:0000305|PubMed:26860543}. EcoCyc product frame: SBMA-MONOMER. Genomic coordinates: 396639-397859.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFY6|protein.P0AFY6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=sbmA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001297,ECOCYC:EG10928,GeneID:946884`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:396639-397859:+; feature_type=gene
