---
entity_id: "gene.b2831"
entity_type: "gene"
name: "mutH"
source_database: "NCBI RefSeq"
source_id: "gene-b2831"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2831"
  - "mutH"
---

# mutH

`gene.b2831`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2831`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mutH (gene.b2831) is a gene entity. It encodes mutH (protein.P06722). Encoded protein function: FUNCTION: Sequence-specific endonuclease that cleaves unmethylated GATC sequences. It is involved in DNA mismatch repair. EcoCyc product frame: EG10624-MONOMER. EcoCyc synonyms: mutR, prv. Genomic coordinates: 2969662-2970351.

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06722|protein.P06722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009287,ECOCYC:EG10624,GeneID:947299`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2969662-2970351:+; feature_type=gene
