---
entity_id: "gene.b2154"
entity_type: "gene"
name: "yeiG"
source_database: "NCBI RefSeq"
source_id: "gene-b2154"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2154"
  - "yeiG"
---

# yeiG

`gene.b2154`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2154`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiG (gene.b2154) is a gene entity. It encodes yeiG (protein.P33018). Encoded protein function: FUNCTION: Serine hydrolase involved in the detoxification of formaldehyde. Hydrolyzes S-formylglutathione to glutathione and formate. Also shows esterase activity against alpha-naphthyl acetate, lactoylglutathione, palmitoyl-CoA and several pNP-esters of short chain fatty acids. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16567800}. EcoCyc product frame: EG12026-MONOMER. Genomic coordinates: 2243910-2244746. EcoCyc protein note: YeiG is a promiscuous serine hydrolase; its highest specific activity is with the substrate S-formylglutathione. Sulfhydryl inhibitors affect enzymatic activity . A general esterase activity of YeiG was first discovered in a high-throughput screen of purified proteins . YeiG also has significant activity with the substrate lactoylglutathione, an intermediate of the detoxification of methylglyoxal. It may thus represent a cytoplasmic equivalent of glyoxalase II, which may be involved in the detoxification of endogenous methylglyoxal . YeiG has similarity to S-formylglutathione hydrolases of Arabidopsis, S. cerevisiae, human, and a paralog, FrmB . yeiG is expressed constitutively in both the wild type and frmB deletion background. Under normal growth conditions, neither a yeiG deletion mutant nor a frmB yeiG double mutant have a detectable growth defect...

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33018|protein.P33018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007124,ECOCYC:EG12026,GeneID:949045`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2243910-2244746:+; feature_type=gene
