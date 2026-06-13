---
entity_id: "gene.b4097"
entity_type: "gene"
name: "phnK"
source_database: "NCBI RefSeq"
source_id: "gene-b4097"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4097"
  - "phnK"
---

# phnK

`gene.b4097`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4097`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnK (gene.b4097) is a gene entity. It encodes phnK (protein.P16678). Encoded protein function: FUNCTION: Belongs to an operon involved in alkylphosphonate uptake and C-P lyase. Exact function not known. PhnK is not required for the ribophosphonate triphosphate (RPnTP) synthase reaction. EcoCyc product frame: PHNK-MONOMER. Genomic coordinates: 4318006-4318764.

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16678|protein.P16678]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnK; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013424,ECOCYC:EG10720,GeneID:948611`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4318006-4318764:-; feature_type=gene
