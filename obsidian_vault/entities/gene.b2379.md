---
entity_id: "gene.b2379"
entity_type: "gene"
name: "alaC"
source_database: "NCBI RefSeq"
source_id: "gene-b2379"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2379"
  - "alaC"
---

# alaC

`gene.b2379`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2379`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alaC (gene.b2379) is a gene entity. It encodes alaC (protein.P77434). Encoded protein function: FUNCTION: Involved in the biosynthesis of alanine (PubMed:20729367). Catalyzes the transamination of pyruvate by glutamate, leading to the formation of L-alanine and 2-oxoglutarate. Is also able to catalyze the reverse reaction (PubMed:20729367). {ECO:0000269|PubMed:20729367, ECO:0000269|PubMed:21597182}. EcoCyc product frame: G7242-MONOMER. EcoCyc synonyms: yfdZ. Genomic coordinates: 2497057-2498295.

## Biological Role

Repressed by nac (protein.Q47005). Activated by sgrR (protein.P33595).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77434|protein.P77434]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `S` - regulator=SgrR; target=alaC; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=alaC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007850,ECOCYC:G7242,GeneID:946850`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2497057-2498295:-; feature_type=gene
