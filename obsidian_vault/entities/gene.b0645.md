---
entity_id: "gene.b0645"
entity_type: "gene"
name: "ybeR"
source_database: "NCBI RefSeq"
source_id: "gene-b0645"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0645"
  - "ybeR"
---

# ybeR

`gene.b0645`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0645`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeR (gene.b0645) is a gene entity. It encodes ybeR (protein.P77627). Encoded protein function: Uncharacterized protein YbeR EcoCyc product frame: G6352-MONOMER. Genomic coordinates: 676711-677418. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 12, 2017.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77627|protein.P77627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybeR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002208,ECOCYC:G6352,GeneID:945249`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:676711-677418:+; feature_type=gene
