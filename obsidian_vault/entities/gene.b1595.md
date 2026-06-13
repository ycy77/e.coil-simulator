---
entity_id: "gene.b1595"
entity_type: "gene"
name: "ynfL"
source_database: "NCBI RefSeq"
source_id: "gene-b1595"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1595"
  - "ynfL"
---

# ynfL

`gene.b1595`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1595`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfL (gene.b1595) is a gene entity. It encodes ynfL (protein.P77559). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YnfL EcoCyc product frame: G6853-MONOMER. Genomic coordinates: 1668699-1669592. EcoCyc protein note: Expression of cloned ynfLM in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) confers hypersensitivity to acriflavine (minimum inhibitory concentration, 12.5 µg/mL for KAM3 versus 3.13 µg/mL for KAM3/pUCynfLM) but overexpression of ynfM alone (KAM3/pTrcHynfM) does not, suggesting that the sensitivity phenotype results from the expression of ynfL . YnfL was predicted to be a LysR-type transcription factor . This protein contains a helix-turn-helix motif to bind DNA in its N-terminal domain . YnfL DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . The functional analysis of YnfL-binding targets suggests that it is involved in regulation of arabinose efflux . However, the effect of YnfL on the transcription of any gene has not yet been demonstrated . Upstream of the ynfL gene, a sequence was found that could work as a transcriptional promoter .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77559|protein.P77559]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005326,ECOCYC:G6853,GeneID:946136`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1668699-1669592:-; feature_type=gene
