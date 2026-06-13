---
entity_id: "gene.b1270"
entity_type: "gene"
name: "btuR"
source_database: "NCBI RefSeq"
source_id: "gene-b1270"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1270"
  - "btuR"
---

# btuR

`gene.b1270`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1270`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btuR (gene.b1270) is a gene entity. It encodes btuR (protein.P0A9H5). Encoded protein function: FUNCTION: Required for both de novo synthesis of the corrin ring for the assimilation of exogenous corrinoids. Participates in the adenosylation of a variety of incomplete and complete corrinoids (By similarity). {ECO:0000250}. EcoCyc product frame: COBALADENOSYLTRANS-MONOMER. EcoCyc synonyms: cobA. Genomic coordinates: 1327767-1328357. EcoCyc protein note: E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . Sequence similarity and complementation of a cobA mutant in Salmonella typhimurium suggests that btuR encodes the cobinamide adenosyltransferase . Cobinamide adenosyltransferase catalyzes the synthesis of adenosylcobalamin from a cobalamin precursor transported into the cell . A btuR mutation leads to loss of repression of expression by externally supplied vitamin B12 and was therefore initially thought to encode a transcriptional repressor of btuB . However, it was later shown that a btuR mutation results in a decrease in the pool of intracellular adenosylcobalamin and is thus more likely involved in the conversion of vitamin B12 to adenosylcobalamin . Insertion mutants within btuR lead to an inability to utilize cobinamide under aerobic growth conditions...

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9H5|protein.P0A9H5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004261,ECOCYC:EG10130,GeneID:945839`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1327767-1328357:-; feature_type=gene
