---
entity_id: "gene.b3087"
entity_type: "gene"
name: "ygjR"
source_database: "NCBI RefSeq"
source_id: "gene-b3087"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3087"
  - "ygjR"
---

# ygjR

`gene.b3087`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3087`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygjR (gene.b3087) is a gene entity. It encodes ygjR (protein.P42599). Encoded protein function: Uncharacterized oxidoreductase YgjR (EC 1.-.-.-) EcoCyc product frame: G7606-MONOMER. Genomic coordinates: 3237311-3238297. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 7, 2017.

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42599|protein.P42599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010148,ECOCYC:G7606,GeneID:947600`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3237311-3238297:+; feature_type=gene
