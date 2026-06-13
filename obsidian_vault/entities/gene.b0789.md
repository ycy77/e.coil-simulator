---
entity_id: "gene.b0789"
entity_type: "gene"
name: "clsB"
source_database: "NCBI RefSeq"
source_id: "gene-b0789"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0789"
  - "clsB"
---

# clsB

`gene.b0789`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0789`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clsB (gene.b0789) is a gene entity. It encodes clsB (protein.P0AA84). Encoded protein function: FUNCTION: Catalyzes the phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol. Can also catalyze phosphatidyl group transfer to water to form phosphatidate. {ECO:0000255|HAMAP-Rule:MF_01917, ECO:0000269|PubMed:10634942, ECO:0000269|PubMed:22988102}. EcoCyc product frame: G6406-MONOMER. EcoCyc synonyms: ybhO. Genomic coordinates: 822498-823739. EcoCyc protein note: ClsB is the second cardiolipin synthase in E. coli . Synthesis of cardiolipin during exponential growth is due to the activity of CARDIOLIPSYN-MONOMER ClsA, while all three cardiolipin synthases, ClsA, ClsB and G6551-MONOMER ClsC, contribute to cardiolipin synthesis in stationary phase . ClsB is able to catalyze synthesis of phosphatidylglycerol from phosphatidylethanolamine and glycerol and appears to be involved in the biosynthesis of 6-phosphatidyltrehalose and 6,6'-diphosphatidyltrehalose in certain E. coli strains . Cells with deletions of all three of the genes encoding cardiolipin synthases, ΔclsABC, completely lack cardiolipin...

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA84|protein.P0AA84]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002692,ECOCYC:G6406,GeneID:945409`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:822498-823739:-; feature_type=gene
