---
entity_id: "gene.b2947"
entity_type: "gene"
name: "gshB"
source_database: "NCBI RefSeq"
source_id: "gene-b2947"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2947"
  - "gshB"
---

# gshB

`gene.b2947`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2947`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gshB (gene.b2947) is a gene entity. It encodes gshB (protein.P04425). Encoded protein function: Glutathione synthetase (EC 6.3.2.3) (GSH synthetase) (GSH-S) (GSHase) (Glutathione synthase) EcoCyc product frame: GLUTATHIONE-SYN-MONOMER. EcoCyc synonyms: gsh-II. Genomic coordinates: 3091878-3092828.

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04425|protein.P04425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009667,ECOCYC:EG10419,GeneID:947445`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3091878-3092828:+; feature_type=gene
