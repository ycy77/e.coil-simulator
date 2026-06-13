---
entity_id: "gene.b0769"
entity_type: "gene"
name: "ybhH"
source_database: "NCBI RefSeq"
source_id: "gene-b0769"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0769"
  - "ybhH"
---

# ybhH

`gene.b0769`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0769`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhH (gene.b0769) is a gene entity. It encodes ybhH (protein.P0AAV8). Encoded protein function: Putative isomerase YbhH (EC 5.-.-.-) EcoCyc product frame: G6399-MONOMER. Genomic coordinates: 800759-801811. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 12, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAV8|protein.P0AAV8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybhH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002618,ECOCYC:G6399,GeneID:945375`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:800759-801811:+; feature_type=gene
