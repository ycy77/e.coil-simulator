---
entity_id: "gene.b1652"
entity_type: "gene"
name: "rnt"
source_database: "NCBI RefSeq"
source_id: "gene-b1652"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1652"
  - "rnt"
---

# rnt

`gene.b1652`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1652`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnt (gene.b1652) is a gene entity. It encodes rnt (protein.P30014). Encoded protein function: FUNCTION: Trims short 3' overhangs of a variety of RNA species, leaving a one or two nucleotide 3' overhang. Responsible for the end-turnover of tRNA: specifically removes the terminal AMP residue from uncharged tRNA (tRNA-C-C-A). Also appears to be involved in tRNA biosynthesis, especially in strains lacking other exoribonucleases. {ECO:0000255|HAMAP-Rule:MF_00157, ECO:0000269|PubMed:12364334, ECO:0000269|PubMed:17437714, ECO:0000269|PubMed:21317904}.; FUNCTION: A general regulator of small RNAs (sRNA), contributes to their degradation. Upon overexpression suppresses sRNA-mediated RhyB-silencing of multiple RNA targets; overexpression leads to nearly complete loss of RhyB sRNA. {ECO:0000269|PubMed:34210798}. EcoCyc product frame: EG11547-MONOMER. Genomic coordinates: 1728347-1728994.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30014|protein.P30014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005523,ECOCYC:EG11547,GeneID:946159`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1728347-1728994:+; feature_type=gene
