---
entity_id: "gene.b1636"
entity_type: "gene"
name: "pdxY"
source_database: "NCBI RefSeq"
source_id: "gene-b1636"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1636"
  - "pdxY"
---

# pdxY

`gene.b1636`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1636`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxY (gene.b1636) is a gene entity. It encodes pdxY (protein.P77150). Encoded protein function: FUNCTION: Pyridoxal kinase involved in the salvage pathway of pyridoxal 5'-phosphate (PLP). Catalyzes the phosphorylation of pyridoxal to PLP in vivo, but shows very low activity compared to PdxK. Displays a low level of pyridoxine kinase activity when overexpressed, which is however not physiologically relevant. {ECO:0000269|PubMed:15249053, ECO:0000269|PubMed:9537380}. EcoCyc product frame: PDXY-MONOMER. EcoCyc synonyms: ydgS. Genomic coordinates: 1715026-1715889.

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77150|protein.P77150]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005475,ECOCYC:G6879,GeneID:946162`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1715026-1715889:-; feature_type=gene
