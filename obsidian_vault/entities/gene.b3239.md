---
entity_id: "gene.b3239"
entity_type: "gene"
name: "yhcO"
source_database: "NCBI RefSeq"
source_id: "gene-b3239"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3239"
  - "yhcO"
---

# yhcO

`gene.b3239`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3239`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhcO (gene.b3239) is a gene entity. It encodes yhcO (protein.P64616). Encoded protein function: Ribonuclease inhibitor barstar-like protein YhcO EcoCyc product frame: G7684-MONOMER. Genomic coordinates: 3385857-3386129. EcoCyc protein note: No information about this protein was found by a literature search conducted on January 19, 2010.

## Biological Role

Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64616|protein.P64616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010625,ECOCYC:G7684,GeneID:947830`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3385857-3386129:-; feature_type=gene
