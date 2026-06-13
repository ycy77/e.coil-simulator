---
entity_id: "gene.b0927"
entity_type: "gene"
name: "gloC"
source_database: "NCBI RefSeq"
source_id: "gene-b0927"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0927"
  - "gloC"
---

# gloC

`gene.b0927`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0927`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gloC (gene.b0927) is a gene entity. It encodes gloC (protein.P75849). Encoded protein function: FUNCTION: Type II glyoxalase, isozyme of GloB, that hydrolyzes (R)-S-lactoylglutathione to (R)-lactate and glutathione. Plays a minor contribution to methylglyoxal (MG) detoxification in E.coli, compared to GloB. The two isoenzymes have additive effects and ensure maximal MG degradation. {ECO:0000269|PubMed:25670698}. EcoCyc product frame: G6475-MONOMER. EcoCyc synonyms: ycbL. Genomic coordinates: 983650-984297. EcoCyc protein note: GloC is a type II glyoxalase that is an isozyme of GLYOXII-MONOMER GloB. It plays a minor role in methylglyoxal detoxification . The metal binding properties of the ortholog from Salmonella enterica serovar typhimurium 14028s have been studied . The S. enterica enzyme was found to have glyoxalase II activity . Single gloB and gloC mutants show decreased methylglyoxal tolerance; a ΔgloBC double deletion mutant is more sensitive to methylglyoxal than either single mutant . GloC in E. coli was shown to interact with the enzyme G7767-MONOMER in a protein-enzyme interactions (PEIs) study that examined the connection between protein-protein interactions (PPIs) and metabolomics networks studied in 22 different environmental conditions...

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75849|protein.P75849]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003147,ECOCYC:G6475,GeneID:945551`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:983650-984297:+; feature_type=gene
