---
entity_id: "gene.b1583"
entity_type: "gene"
name: "ynfB"
source_database: "NCBI RefSeq"
source_id: "gene-b1583"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1583"
  - "ynfB"
---

# ynfB

`gene.b1583`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1583`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfB (gene.b1583) is a gene entity. It encodes ynfB (protein.P76170). Encoded protein function: UPF0482 protein YnfB EcoCyc product frame: G6841-MONOMER. Genomic coordinates: 1655808-1656149. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 12, 2017.

## Biological Role

Repressed by gadX (protein.P37639). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76170|protein.P76170]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynfB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=ynfB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005284,ECOCYC:G6841,GeneID:946119`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1655808-1656149:+; feature_type=gene
