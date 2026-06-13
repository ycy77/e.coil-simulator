---
entity_id: "gene.b2768"
entity_type: "gene"
name: "ygcP"
source_database: "NCBI RefSeq"
source_id: "gene-b2768"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2768"
  - "ygcP"
---

# ygcP

`gene.b2768`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2768`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygcP (gene.b2768) is a gene entity. It encodes ygcP (protein.Q46906). Encoded protein function: Putative anti-terminator regulatory protein YgcP EcoCyc product frame: G7434-MONOMER. Genomic coordinates: 2894196-2894771. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 26, 2011.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46906|protein.Q46906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygcP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009074,ECOCYC:G7434,GeneID:947536`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2894196-2894771:+; feature_type=gene
