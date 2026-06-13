---
entity_id: "gene.b2771"
entity_type: "gene"
name: "ygcS"
source_database: "NCBI RefSeq"
source_id: "gene-b2771"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2771"
  - "ygcS"
---

# ygcS

`gene.b2771`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2771`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygcS (gene.b2771) is a gene entity. It encodes ygcS (protein.Q46909). Encoded protein function: Inner membrane metabolite transport protein YgcS EcoCyc product frame: B2771-MONOMER. Genomic coordinates: 2896533-2897870. EcoCyc protein note: The YgcS protein is an uncharacterised member of the Sugar Porter (SP) family of transporters within the Major Facilitator Superfamily (MFS) .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46909|protein.Q46909]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ygcS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009082,ECOCYC:G7437,GeneID:947238`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2896533-2897870:-; feature_type=gene
