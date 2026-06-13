---
entity_id: "gene.b4053"
entity_type: "gene"
name: "alr"
source_database: "NCBI RefSeq"
source_id: "gene-b4053"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4053"
  - "alr"
---

# alr

`gene.b4053`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4053`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alr (gene.b4053) is a gene entity. It encodes alr (protein.P0A6B4). Encoded protein function: FUNCTION: Catalyzes the interconversion of L-alanine and D-alanine. Provides the D-alanine required for cell wall biosynthesis. {ECO:0000269|PubMed:18434499}. EcoCyc product frame: ALARACEBIOSYN-MONOMER. EcoCyc synonyms: alr5. Genomic coordinates: 4265782-4266861.

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6B4|protein.P0A6B4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013272,ECOCYC:EG10001,GeneID:948564`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4265782-4266861:+; feature_type=gene
