---
entity_id: "gene.b3644"
entity_type: "gene"
name: "yicC"
source_database: "NCBI RefSeq"
source_id: "gene-b3644"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3644"
  - "yicC"
---

# yicC

`gene.b3644`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3644`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yicC (gene.b3644) is a gene entity. It encodes yicC (protein.P23839). Encoded protein function: FUNCTION: Contributes to degradation of small RNA (sRNA) RhyB. Upon overexpression suppresses sRNA-mediated RhyB-silencing of multiple RNA targets but not other sRNA's targets; overexpression leads to loss of RhyB sRNA. Enables degradation of RhyB by 3' to 5' exoribonuclease PNPase (pnp) (PubMed:34210798). Endonucleolytically cleaves ssRNA, probably generating a 3'-OH and a 5'-phosphate group (PubMed:34815358). {ECO:0000269|PubMed:34210798, ECO:0000269|PubMed:34815358}. EcoCyc product frame: EG11192-MONOMER. Genomic coordinates: 3816676-3817539.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23839|protein.P23839]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011913,ECOCYC:EG11192,GeneID:948154`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3816676-3817539:+; feature_type=gene
