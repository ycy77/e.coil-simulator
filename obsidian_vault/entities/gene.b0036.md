---
entity_id: "gene.b0036"
entity_type: "gene"
name: "caiD"
source_database: "NCBI RefSeq"
source_id: "gene-b0036"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0036"
  - "caiD"
---

# caiD

`gene.b0036`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0036`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

caiD (gene.b0036) is a gene entity. It encodes caiD (protein.P31551). Encoded protein function: FUNCTION: Catalyzes the reversible dehydration of L-carnitinyl-CoA to crotonobetainyl-CoA (PubMed:11551212). Can also hydrate crotonyl-CoA to hydroxybutyryl-CoA (PubMed:11551212). {ECO:0000269|PubMed:11551212}. EcoCyc product frame: CARNRACE-MONOMER. EcoCyc synonyms: yaaL. Genomic coordinates: 35377-36162. EcoCyc protein note: CaiD is a member of the crotonase superfamily; the enzyme purified from E. coli O44:K74 catalyzes the hydration of crotonobetainyl-CoA to carnitinyl-CoA and can use crotonyl-CoA, but not crotonobetaine, as an alternative substrate . CaiD was originally also described as a carnitine racemase; however, only overexpressing both CaiD and CaiE together led to measurable carnitine racemase activity .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31551|protein.P31551]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=caiD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=caiD; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=caiD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000130,ECOCYC:EG11557,GeneID:948995`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:35377-36162:-; feature_type=gene
