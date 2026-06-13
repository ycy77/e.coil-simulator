---
entity_id: "gene.b4252"
entity_type: "gene"
name: "tabA"
source_database: "NCBI RefSeq"
source_id: "gene-b4252"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4252"
  - "tabA"
---

# tabA

`gene.b4252`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4252`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tabA (gene.b4252) is a gene entity. It encodes tabA (protein.P0AF96). Encoded protein function: FUNCTION: Influences biofilm formation. Represses fimbria genes in 8 hours biofilms. May act in response to the combined activity of several toxin-antitoxin (TA) systems. {ECO:0000269|PubMed:19060153}. EcoCyc product frame: G7883-MONOMER. EcoCyc synonyms: yjgK. Genomic coordinates: 4474862-4475314. EcoCyc protein note: The toxin-antitoxin biofilm protein TabA may decrease biofilm dispersal in response to the combined activity of several toxin-antitoxin (TA) systems. Simultaneous deletion of five TA systems leads to increased expression of tabA. Overexpression of tabA leads to decreased biofilm formation at 8 hours, but increased biofilm formation by 24 hours; deletion of tabA has the opposite effect. At 8 hours, deletion of tabA increases expression of fimbriae-associated genes . Transcription of tabA was predicted to be regulated by KdgR . TabA: "toxin-antitoxin biofilm protein"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF96|protein.P0AF96]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013921,ECOCYC:G7883,GeneID:948777`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4474862-4475314:+; feature_type=gene
