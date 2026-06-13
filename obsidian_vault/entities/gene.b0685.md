---
entity_id: "gene.b0685"
entity_type: "gene"
name: "ybfE"
source_database: "NCBI RefSeq"
source_id: "gene-b0685"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0685"
  - "ybfE"
---

# ybfE

`gene.b0685`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0685`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybfE (gene.b0685) is a gene entity. It encodes ybfE (protein.P0AAU7). Encoded protein function: Uncharacterized protein YbfE EcoCyc product frame: EG11775-MONOMER. Genomic coordinates: 711605-711898. EcoCyc protein note: Levels of ybfE mRNA are increased by exposure to the DNA damaging agent mitomycin C; the increase is dependent on LexA. A putative LexA binding site with a very high "heterology index" (HI) score has been identified upstream of the YbfE open reading frame . Expression of a ybfE transcriptional fusion increases upon exposure to the alkylating agents chlorocetaldehyde and styrene oxide; an E. coli MG1655 strain lacking ybfE (AB11157 ybfE::kan) is significantly more sensitive to both these agents compared to wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAU7|protein.P0AAU7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002335,ECOCYC:EG11775,GeneID:945291`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:711605-711898:-; feature_type=gene
