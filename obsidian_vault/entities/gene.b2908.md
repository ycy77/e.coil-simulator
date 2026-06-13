---
entity_id: "gene.b2908"
entity_type: "gene"
name: "pepP"
source_database: "NCBI RefSeq"
source_id: "gene-b2908"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2908"
  - "pepP"
---

# pepP

`gene.b2908`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2908`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pepP (gene.b2908) is a gene entity. It encodes pepP (protein.P15034). Encoded protein function: Xaa-Pro aminopeptidase (EC 3.4.11.9) (Aminoacylproline aminopeptidase) (Aminopeptidase P II) (APP-II) (X-Pro aminopeptidase) EcoCyc product frame: EG10697-MONOMER. Genomic coordinates: 3053515-3054840.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15034|protein.P15034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pepP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009549,ECOCYC:EG10697,GeneID:947385`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3053515-3054840:-; feature_type=gene
