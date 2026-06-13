---
entity_id: "gene.b2472"
entity_type: "gene"
name: "dapE"
source_database: "NCBI RefSeq"
source_id: "gene-b2472"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2472"
  - "dapE"
---

# dapE

`gene.b2472`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2472`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dapE (gene.b2472) is a gene entity. It encodes dapE (protein.P0AED7). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of N-succinyl-L,L-diaminopimelic acid (SDAP), forming succinate and LL-2,6-diaminopimelate (DAP), an intermediate involved in the bacterial biosynthesis of lysine and meso-diaminopimelic acid, an essential component of bacterial cell walls. {ECO:0000269|PubMed:3276674}. EcoCyc product frame: MONOMER0-1981. EcoCyc synonyms: msgB. Genomic coordinates: 2591607-2592734.

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AED7|protein.P0AED7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008142,ECOCYC:EG10208,GeneID:948313`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2591607-2592734:+; feature_type=gene
