---
entity_id: "gene.b3077"
entity_type: "gene"
name: "ebgC"
source_database: "NCBI RefSeq"
source_id: "gene-b3077"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3077"
  - "ebgC"
---

# ebgC

`gene.b3077`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3077`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ebgC (gene.b3077) is a gene entity. It encodes ebgC (protein.P0AC73). Encoded protein function: FUNCTION: Required for full activity of the EbgA enzyme. Exact function not known. EcoCyc product frame: EG10253-MONOMER. Genomic coordinates: 3225722-3226171.

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC73|protein.P0AC73]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010106,ECOCYC:EG10253,GeneID:947581`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3225722-3226171:+; feature_type=gene
