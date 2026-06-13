---
entity_id: "gene.b2893"
entity_type: "gene"
name: "dsbC"
source_database: "NCBI RefSeq"
source_id: "gene-b2893"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2893"
  - "dsbC"
---

# dsbC

`gene.b2893`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2893`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsbC (gene.b2893) is a gene entity. It encodes dsbC (protein.P0AEG6). Encoded protein function: FUNCTION: Acts as a disulfide isomerase, interacting with incorrectly folded proteins to correct non-native disulfide bonds. DsbG and DsbC are part of a periplasmic reducing system that controls the level of cysteine sulfenylation, and provides reducing equivalents to rescue oxidatively damaged secreted proteins. Acts by transferring its disulfide bond to other proteins and is reduced in the process. DsbC is reoxidized by DsbD. {ECO:0000269|PubMed:19965429}. EcoCyc product frame: DSBC-MONOMER. EcoCyc synonyms: xprA. Genomic coordinates: 3038112-3038822.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEG6|protein.P0AEG6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=dsbC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009494,ECOCYC:EG11070,GeneID:947363`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3038112-3038822:-; feature_type=gene
