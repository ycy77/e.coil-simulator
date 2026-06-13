---
entity_id: "gene.b0234"
entity_type: "gene"
name: "yafP"
source_database: "NCBI RefSeq"
source_id: "gene-b0234"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0234"
  - "yafP"
---

# yafP

`gene.b0234`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0234`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafP (gene.b0234) is a gene entity. It encodes yafP (protein.Q47158). Encoded protein function: Uncharacterized N-acetyltransferase YafP (EC 2.3.1.-) EcoCyc product frame: G6118-MONOMER. Genomic coordinates: 252709-253161. EcoCyc protein note: YafP is not a part of the YafO-YafN toxin-antitoxin system . Polar dinB mutations affecting the dinB-yafN-yafO-yafP operon reduce spontaneous mutagenesis ; however, only DinB is required for stress-induced mutagenesis . The function of YafP in the uropathogenic strain E. coli CFT073 has been studied - results suggest YafP may have a role in the metabolic transformation of carcinogenic compounds .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47158|protein.Q47158]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000801,ECOCYC:G6118,GeneID:944912`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:252709-253161:+; feature_type=gene
