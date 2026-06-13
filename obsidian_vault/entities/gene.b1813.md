---
entity_id: "gene.b1813"
entity_type: "gene"
name: "nudL"
source_database: "NCBI RefSeq"
source_id: "gene-b1813"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1813"
  - "nudL"
---

# nudL

`gene.b1813`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1813`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudL (gene.b1813) is a gene entity. It encodes nudL (protein.P43337). Encoded protein function: FUNCTION: Probably mediates the hydrolysis of some nucleoside diphosphate derivatives. {ECO:0000255|HAMAP-Rule:MF_01592}. EcoCyc product frame: EG12693-MONOMER. EcoCyc synonyms: yeaB. Genomic coordinates: 1896170-1896748. EcoCyc protein note: NudL belongs to the Nudix family of hydrolases and was predicted to have CoA pyrophosphohydrolase activity . nudL (yeaB) was isolated as a multicopy suppressor of the repression of flhDC transcription in a pgsA mutant. The suppression may be due to the reduction of σS expression in cells that overexpress nudL . nudL (yeaB) was also isolated as a multicopy suppressor of the PLP auxotrophy of a pdxB deletion strain. NudL was found to be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 4-PHOSPHONOOXY-THREONINE, that lies downstream of PdxB. The pathway diverts 3-phosphohydroxypyruvate from serine biosynthesis. With a Kcat of 5.7x10-5, NudL is an inefficient catalyst of the conversion of 3-phosphohydroxypyruvate to hydroxypyruvate, but its activity appears to be sufficient for production of PLP . Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43337|protein.P43337]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006035,ECOCYC:EG12693,GeneID:946330`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1896170-1896748:+; feature_type=gene
