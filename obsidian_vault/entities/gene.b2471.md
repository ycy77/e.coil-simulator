---
entity_id: "gene.b2471"
entity_type: "gene"
name: "yffB"
source_database: "NCBI RefSeq"
source_id: "gene-b2471"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2471"
  - "yffB"
---

# yffB

`gene.b2471`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2471`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yffB (gene.b2471) is a gene entity. It encodes yffB (protein.P24178). Encoded protein function: Protein YffB EcoCyc product frame: EG11147-MONOMER. Genomic coordinates: 2591247-2591603. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 16, 2017.

## Biological Role

Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24178|protein.P24178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=yffB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008140,ECOCYC:EG11147,GeneID:946953`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2591247-2591603:+; feature_type=gene
