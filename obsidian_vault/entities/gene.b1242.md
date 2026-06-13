---
entity_id: "gene.b1242"
entity_type: "gene"
name: "ychE"
source_database: "NCBI RefSeq"
source_id: "gene-b1242"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1242"
  - "ychE"
---

# ychE

`gene.b1242`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1242`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ychE (gene.b1242) is a gene entity. It encodes ychE (protein.P25743). Encoded protein function: UPF0056 membrane protein YhcE EcoCyc product frame: EG11342-MONOMER. Genomic coordinates: 1298598-1299245. EcoCyc protein note: YchE is an inner membrane protein with six predicted transmembrane domains. The C terminus is located in the periplasm . YchE, YhgN and MarC are paralogs. MarC was thought to be involved in multiple antibiotic resistance, but neither a marC single deletion mutant nor a triple marC ychE yhgN deletion mutant shows a difference in susceptibility to various antibiotics compared to wild type .

## Biological Role

Repressed by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25743|protein.P25743]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004168,ECOCYC:EG11342,GeneID:945836`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1298598-1299245:+; feature_type=gene
