---
entity_id: "gene.b0040"
entity_type: "gene"
name: "caiT"
source_database: "NCBI RefSeq"
source_id: "gene-b0040"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0040"
  - "caiT"
---

# caiT

`gene.b0040`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0040`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiT (gene.b0040) is a gene entity. It encodes caiT (protein.P31553). Encoded protein function: FUNCTION: Catalyzes the exchange of L-carnitine for gamma-butyrobetaine (PubMed:12163501, PubMed:20829798, PubMed:30846799). Can also transport D-carnitine and, with lower efficiency, acetyl-L-carnitine and glycine betaine (PubMed:12163501). {ECO:0000269|PubMed:12163501, ECO:0000269|PubMed:20829798, ECO:0000269|PubMed:30846799}. EcoCyc product frame: CAIT-MONOMER. EcoCyc synonyms: yaaP. Genomic coordinates: 40417-41931.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31553|protein.P31553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=caiT; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=caiT; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=caiT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000141,ECOCYC:EG11561,GeneID:944765`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:40417-41931:-; feature_type=gene
