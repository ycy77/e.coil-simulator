---
entity_id: "gene.b3934"
entity_type: "gene"
name: "cytR"
source_database: "NCBI RefSeq"
source_id: "gene-b3934"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3934"
  - "cytR"
---

# cytR

`gene.b3934`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3934`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cytR (gene.b3934) is a gene entity. It encodes cytR (protein.P0ACN7). Encoded protein function: FUNCTION: This protein negatively controls the transcription initiation of genes such as deoCABD, udp, and cdd encoding catabolizing enzymes and nupC, nupG, and tsx encoding transporting and pore-forming proteins. Binds cytidine and adenosine as effectors. EcoCyc product frame: PD04028. Genomic coordinates: 4123431-4124456.

## Biological Role

Repressed by crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACN7|protein.P0ACN7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=cytR; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=cytR; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `S` - regulator=CytR; target=cytR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012853,ECOCYC:EG10200,GeneID:948427`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4123431-4124456:-; feature_type=gene
