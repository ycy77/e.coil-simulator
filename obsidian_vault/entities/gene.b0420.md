---
entity_id: "gene.b0420"
entity_type: "gene"
name: "dxs"
source_database: "NCBI RefSeq"
source_id: "gene-b0420"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0420"
  - "dxs"
---

# dxs

`gene.b0420`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0420`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dxs (gene.b0420) is a gene entity. It encodes dxs (protein.P77488). Encoded protein function: FUNCTION: Catalyzes the acyloin condensation reaction between C atoms 2 and 3 of pyruvate and glyceraldehyde 3-phosphate to yield 1-deoxy-D-xylulose-5-phosphate (DXP). {ECO:0000269|PubMed:17135236, ECO:0000269|PubMed:9371765, ECO:0000269|PubMed:9482846}. EcoCyc product frame: DXS-MONOMER. EcoCyc synonyms: yajP. Genomic coordinates: 438315-440177.

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77488|protein.P77488]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001461,ECOCYC:G6237,GeneID:945060`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:438315-440177:-; feature_type=gene
