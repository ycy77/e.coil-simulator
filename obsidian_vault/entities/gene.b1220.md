---
entity_id: "gene.b1220"
entity_type: "gene"
name: "ychO"
source_database: "NCBI RefSeq"
source_id: "gene-b1220"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1220"
  - "ychO"
---

# ychO

`gene.b1220`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1220`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ychO (gene.b1220) is a gene entity. It encodes ychO (protein.P39165). Encoded protein function: Uncharacterized protein YchO EcoCyc product frame: EG12405-MONOMER. EcoCyc synonyms: ychP. Genomic coordinates: 1273784-1275178. EcoCyc protein note: In the avian pathogenic E. coli (APEC) strain SEPT362, the orthologous ychO gene plays a role in pathogenicity . In a large genetic interaction screen, ychO showed genetic interactions with a number of proteins involved in translation and ribosome biogenesis. A ΔychO mutant shows increased levels of stop codon readthrough .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39165|protein.P39165]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004095,ECOCYC:EG12405,GeneID:945801`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1273784-1275178:+; feature_type=gene
