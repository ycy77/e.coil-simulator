---
entity_id: "gene.b4118"
entity_type: "gene"
name: "melR"
source_database: "NCBI RefSeq"
source_id: "gene-b4118"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4118"
  - "melR"
---

# melR

`gene.b4118`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4118`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

melR (gene.b4118) is a gene entity. It encodes melR (protein.P0ACH8). Encoded protein function: FUNCTION: Transcription activator for the expression of the melAB operon. MelR binds at two sites located upstream of the melAB transcription site. {ECO:0000269|PubMed:2684786}. EcoCyc product frame: PD00208. Genomic coordinates: 4340720-4341628.

## Biological Role

Repressed by melR (protein.P0ACH8). Activated by rpoD (protein.P00579), melR (protein.P0ACH8), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACH8|protein.P0ACH8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=melR; function=+
- `activates` <-- [[protein.P0ACH8|protein.P0ACH8]] `RegulonDB` `C` - regulator=MelR; target=melR; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=melR; function=+
- `represses` <-- [[protein.P0ACH8|protein.P0ACH8]] `RegulonDB` `C` - regulator=MelR; target=melR; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0013486,ECOCYC:EG11230,GeneID:948637`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4340720-4341628:-; feature_type=gene
