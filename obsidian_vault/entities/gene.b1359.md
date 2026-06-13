---
entity_id: "gene.b1359"
entity_type: "gene"
name: "ydaU"
source_database: "NCBI RefSeq"
source_id: "gene-b1359"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1359"
  - "ydaU"
---

# ydaU

`gene.b1359`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1359`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydaU (gene.b1359) is a gene entity. It encodes ydaU (protein.P76065). Encoded protein function: Uncharacterized protein YdaU EcoCyc product frame: G6683-MONOMER. Genomic coordinates: 1421119-1421976. EcoCyc protein note: A ΔydaU mutant has aggravating genetic interactions with genes involved in DNA recombination .

## Biological Role

Repressed by racR (protein.P76062). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76065|protein.P76065]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydaU; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P76062|protein.P76062]] `RegulonDB` `S` - regulator=RacR; target=ydaU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004558,ECOCYC:G6683,GeneID:945925`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1421119-1421976:+; feature_type=gene
