---
entity_id: "gene.b0608"
entity_type: "gene"
name: "ybdR"
source_database: "NCBI RefSeq"
source_id: "gene-b0608"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0608"
  - "ybdR"
---

# ybdR

`gene.b0608`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0608`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdR (gene.b0608) is a gene entity. It encodes ybdR (protein.P77316). Encoded protein function: Uncharacterized zinc-type alcohol dehydrogenase-like protein YbdR (EC 1.-.-.-) EcoCyc product frame: G6335-MONOMER. Genomic coordinates: 642088-643326. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 21, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77316|protein.P77316]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybdR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002099,ECOCYC:G6335,GeneID:949067`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:642088-643326:+; feature_type=gene
