---
entity_id: "gene.b0117"
entity_type: "gene"
name: "yacH"
source_database: "NCBI RefSeq"
source_id: "gene-b0117"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0117"
  - "yacH"
---

# yacH

`gene.b0117`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0117`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yacH (gene.b0117) is a gene entity. It encodes yacH (protein.P36682). Encoded protein function: Uncharacterized protein YacH EcoCyc product frame: EG12315-MONOMER. Genomic coordinates: 129407-131260. EcoCyc protein note: Construction of a strain in which yacH is replaced by an FRT-lacZ-aph-FRT cassette has been described . yacH may encode a membrane protein; yacH transcription is reduced upon exposure to a sublethal dose of the cationic antimicrobial insect peptide, cecropin A .

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36682|protein.P36682]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000406,ECOCYC:EG12315,GeneID:944868`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:129407-131260:-; feature_type=gene
