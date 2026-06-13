---
entity_id: "gene.b1414"
entity_type: "gene"
name: "ydcF"
source_database: "NCBI RefSeq"
source_id: "gene-b1414"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1414"
  - "ydcF"
---

# ydcF

`gene.b1414`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1414`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcF (gene.b1414) is a gene entity. It encodes ydcF (protein.P34209). Encoded protein function: FUNCTION: Binds S-adenosyl-L-methionine (AdoMet). EcoCyc product frame: EG12110-MONOMER. Genomic coordinates: 1487235-1488035. EcoCyc protein note: The function of YdcF is unknown. Evidence from structure and expression analysis suggests that YdcF is an S-adenosylmethionine-dependent enzyme which may play a role in anaerobic respiration . A crystal structure of YdcF has been solved at 1.8 Å resolution. The protein fold shows some similarity to the adenine nucleotide α hydrolase-like family; thus, adenosine-containing compounds were screened for binding. S-adenosylmethionine binds with a dissociation constant of 25 µM .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P34209|protein.P34209]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ydcF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004722,ECOCYC:EG12110,GeneID:946215`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1487235-1488035:+; feature_type=gene
