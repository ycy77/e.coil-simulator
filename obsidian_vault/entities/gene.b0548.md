---
entity_id: "gene.b0548"
entity_type: "gene"
name: "ninE"
source_database: "NCBI RefSeq"
source_id: "gene-b0548"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0548"
  - "ninE"
---

# ninE

`gene.b0548`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0548`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ninE (gene.b0548) is a gene entity. It encodes ninE (protein.Q47270). Encoded protein function: Prophage NinE homolog (Protein NinE homolog from lambdoid prophage DLP12) EcoCyc product frame: G6304-MONOMER. Genomic coordinates: 572921-573091. EcoCyc protein note: NinE has 39% identity to gene products from the nin regions of bacteriophages λ and P22, though it lacks their half-zinc finger domain . A ΔninE mutant has aggravating genetic interactions with genes involved in mismatch repair .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47270|protein.Q47270]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001876,ECOCYC:G6304,GeneID:945151`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:572921-573091:+; feature_type=gene
