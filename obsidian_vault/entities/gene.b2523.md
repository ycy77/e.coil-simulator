---
entity_id: "gene.b2523"
entity_type: "gene"
name: "pepB"
source_database: "NCBI RefSeq"
source_id: "gene-b2523"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2523"
  - "pepB"
---

# pepB

`gene.b2523`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2523`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pepB (gene.b2523) is a gene entity. It encodes pepB (protein.P37095). Encoded protein function: FUNCTION: Probably plays an important role in intracellular peptide degradation (PubMed:20067529). {ECO:0000255|HAMAP-Rule:MF_00504, ECO:0000305|PubMed:20067529}. EcoCyc product frame: EG12310-MONOMER. EcoCyc synonyms: yfhI. Genomic coordinates: 2655075-2656358.

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37095|protein.P37095]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008305,ECOCYC:EG12310,GeneID:948766`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2655075-2656358:-; feature_type=gene
