---
entity_id: "gene.b4155"
entity_type: "gene"
name: "epmA"
source_database: "NCBI RefSeq"
source_id: "gene-b4155"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4155"
  - "epmA"
---

# epmA

`gene.b4155`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4155`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

epmA (gene.b4155) is a gene entity. It encodes epmA (protein.P0A8N7). Encoded protein function: FUNCTION: With EpmB is involved in the beta-lysylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. Catalyzes the ATP-dependent activation of (R)-beta-lysine produced by EpmB, forming a lysyl-adenylate, from which the beta-lysyl moiety is then transferred to the epsilon-amino group of EF-P 'Lys-34'. The substrate (R)-beta-lysine is 100-fold more efficient than either (S)-beta-lysine or L-alpha-lysine. Cannot ligate lysine to any tRNA. {ECO:0000255|HAMAP-Rule:MF_00174, ECO:0000269|PubMed:20729861, ECO:0000269|PubMed:21841797, ECO:0000269|PubMed:22128152}. EcoCyc product frame: EG11211-MONOMER. EcoCyc synonyms: genX, poxA, yjeA. Genomic coordinates: 4382643-4383620.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8N7|protein.P0A8N7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013610,ECOCYC:EG11211,GeneID:948672`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4382643-4383620:+; feature_type=gene
