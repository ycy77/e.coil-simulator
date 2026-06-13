---
entity_id: "gene.b1249"
entity_type: "gene"
name: "clsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1249"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1249"
  - "clsA"
---

# clsA

`gene.b1249`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1249`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clsA (gene.b1249) is a gene entity. It encodes clsA (protein.P0A6H8). Encoded protein function: FUNCTION: Catalyzes the reversible phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol. {ECO:0000255|HAMAP-Rule:MF_00190, ECO:0000269|PubMed:1663113, ECO:0000269|PubMed:22988102}. EcoCyc product frame: CARDIOLIPSYN-MONOMER. EcoCyc synonyms: yciJ, nov, cls. Genomic coordinates: 1307185-1308645. EcoCyc protein note: ClsA is the major cardiolipin synthase in E. coli. Synthesis of cardiolipin during exponential growth is due to the activity of ClsA, while all three cardiolipin synthases, ClsA, G6406-MONOMER ClsB and G6551-MONOMER ClsC, contribute to cardiolipin synthesis in stationary phase . The ClsA protein appears to undergo posttranslational processing at the N terminus . A Δ2-60 deletion mutant retains activity and membrane association . The catalytic domain of ClsA is located in the cytoplasm; ClsA mainly localizes to the cell poles; localization is cardiolipin-dependent...

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6H8|protein.P0A6H8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004186,ECOCYC:EG11608,GeneID:945821`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1307185-1308645:-; feature_type=gene
