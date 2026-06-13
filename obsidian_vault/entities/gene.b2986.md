---
entity_id: "gene.b2986"
entity_type: "gene"
name: "yghT"
source_database: "NCBI RefSeq"
source_id: "gene-b2986"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2986"
  - "yghT"
---

# yghT

`gene.b2986`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2986`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghT (gene.b2986) is a gene entity. It encodes yghT (protein.Q46844). Encoded protein function: Uncharacterized ATP-binding protein YghT EcoCyc product frame: G7552-MONOMER. Genomic coordinates: 3134131-3134823. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 20, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46844|protein.Q46844]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yghT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009798,ECOCYC:G7552,GeneID:947477`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3134131-3134823:+; feature_type=gene
