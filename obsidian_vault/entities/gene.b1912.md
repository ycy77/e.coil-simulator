---
entity_id: "gene.b1912"
entity_type: "gene"
name: "pgsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1912"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1912"
  - "pgsA"
---

# pgsA

`gene.b1912`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1912`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgsA (gene.b1912) is a gene entity. It encodes pgsA (protein.P0ABF8). Encoded protein function: FUNCTION: Catalyzes the conversion of cytidine diphosphate diacylglycerol (CDP-DG) and glycerol 3-phosphate into phosphatidylglycerol (PubMed:3003065, PubMed:8824831). Essential for the synthesis of anionic phospholipids, thereby playing a role in balancing the ratio of zwitterionic and anionic phospholipids, which is thought to be important for normal membrane function (PubMed:3003065, PubMed:8824831). {ECO:0000269|PubMed:3003065, ECO:0000269|PubMed:8824831}. EcoCyc product frame: PHOSPHAGLYPSYN-MONOMER. Genomic coordinates: 1992269-1992817. EcoCyc protein note: Phosphatidylglycerophosphate (PGP) synthase catalyzes the committed step in the biosynthesis of acidic phospholipids. PGP synthase is an integral membrane protein tightly associated with the cytoplasmic membrane . A pgsA null E. coli strain exhibits relatively normal cell division and shows elevated amounts of phospholipid precursors and the normally minimal phospholipid N-acylphosphatidylethanolamine (N-acyl-PE) .

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABF8|protein.P0ABF8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006367,ECOCYC:EG10706,GeneID:945791`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1992269-1992817:-; feature_type=gene
