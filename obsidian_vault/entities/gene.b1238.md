---
entity_id: "gene.b1238"
entity_type: "gene"
name: "tdk"
source_database: "NCBI RefSeq"
source_id: "gene-b1238"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1238"
  - "tdk"
---

# tdk

`gene.b1238`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1238`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdk (gene.b1238) is a gene entity. It encodes tdk (protein.P23331). Encoded protein function: FUNCTION: Phosphorylates both thymidine and deoxyuridine. EcoCyc product frame: TDK-MONOMER. Genomic coordinates: 1293527-1294144.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23331|protein.P23331]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004157,ECOCYC:EG10994,GeneID:945834`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1293527-1294144:+; feature_type=gene
