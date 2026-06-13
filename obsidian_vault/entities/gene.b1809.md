---
entity_id: "gene.b1809"
entity_type: "gene"
name: "yoaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1809"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1809"
  - "yoaB"
---

# yoaB

`gene.b1809`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1809`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaB (gene.b1809) is a gene entity. It encodes yoaB (protein.P0AEB7). Encoded protein function: RutC family protein YoaB EcoCyc product frame: G6993-MONOMER. Genomic coordinates: 1893367-1893711. EcoCyc protein note: Transcription of yoaB is induced upon biofilm formation compared to planktonic growth in exponential phase. Induction of expression was found to be dependent on the presence of the F plasmid . A yoaB mutant is impaired in biofilm formation .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEB7|protein.P0AEB7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006020,ECOCYC:G6993,GeneID:946357`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1893367-1893711:+; feature_type=gene
