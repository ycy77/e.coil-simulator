---
entity_id: "gene.b4303"
entity_type: "gene"
name: "sgcQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4303"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4303"
  - "sgcQ"
---

# sgcQ

`gene.b4303`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4303`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgcQ (gene.b4303) is a gene entity. It encodes sgcQ (protein.P39364). Encoded protein function: Putative sgc region protein SgcQ EcoCyc product frame: G7915-MONOMER. EcoCyc synonyms: yjhM. Genomic coordinates: 4528111-4528917. EcoCyc protein note: No information about this protein was found by a literature search conducted on October 11, 2011.

## Biological Role

Repressed by slyA (protein.P0A8W2). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39364|protein.P39364]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgcQ; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=sgcQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014102,ECOCYC:G7915,GeneID:948834`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4528111-4528917:-; feature_type=gene
