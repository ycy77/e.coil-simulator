---
entity_id: "gene.b2797"
entity_type: "gene"
name: "sdaB"
source_database: "NCBI RefSeq"
source_id: "gene-b2797"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2797"
  - "sdaB"
---

# sdaB

`gene.b2797`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2797`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdaB (gene.b2797) is a gene entity. It encodes sdaB (protein.P30744). Encoded protein function: FUNCTION: Also deaminates threonine, particularly when it is present in high concentration. EcoCyc product frame: LSERINEDEAM2-MONOMER. Genomic coordinates: 2929576-2930943. EcoCyc protein note: L-serine deaminase II (SdaB) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. SdaB catalyzes the conversion of L-serine into pyruvate and ammonia . Much like its companion enzyme LSERINEDEAM1-MONOMER, purified SdaB requires activation in vitro with iron and dithiothrietol, suggesting that it, too, has a catalytically important iron-sulfur cluster . Like fellow serine deaminase gene G7624, sdaB is transcribed under glucose-limited conditions in complex medium .

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30744|protein.P30744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009172,ECOCYC:EG11623,GeneID:947262`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2929576-2930943:+; feature_type=gene
