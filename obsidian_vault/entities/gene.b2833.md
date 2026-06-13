---
entity_id: "gene.b2833"
entity_type: "gene"
name: "ygdR"
source_database: "NCBI RefSeq"
source_id: "gene-b2833"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2833"
  - "ygdR"
---

# ygdR

`gene.b2833`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2833`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygdR (gene.b2833) is a gene entity. It encodes ygdR (protein.P65294). Encoded protein function: Uncharacterized lipoprotein YgdR EcoCyc product frame: G7461-MONOMER. Genomic coordinates: 2971271-2971489. EcoCyc protein note: YgdR is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ).

## Biological Role

Repressed by yfeC (protein.P0AD37), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P65294|protein.P65294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0AD37|protein.P0AD37]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ygdR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009293,ECOCYC:G7461,GeneID:947304`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2971271-2971489:+; feature_type=gene
