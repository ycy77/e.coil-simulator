---
entity_id: "gene.b3714"
entity_type: "gene"
name: "adeP"
source_database: "NCBI RefSeq"
source_id: "gene-b3714"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3714"
  - "adeP"
---

# adeP

`gene.b3714`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3714`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adeP (gene.b3714) is a gene entity. It encodes adeP (protein.P31466). Encoded protein function: FUNCTION: High-affinity transporter for adenine. {ECO:0000269|PubMed:24214977, ECO:0000269|PubMed:6198438, ECO:0000269|PubMed:8165228}. EcoCyc product frame: EG11724-MONOMER. EcoCyc synonyms: yieG, purP. Genomic coordinates: 3895272-3896609. EcoCyc protein note: AdeP (formerly PurP) functions in energized high-affinity adenine uptake in Escherichia coli. The process requires the metabolic removal of transported adenine, which prevents the accumulation of adenine inside the cell. There is also a non-energized low-affinity adenine uptake process in an adeP deletion mutant, suggesting the existence of another independent system . Cloned and overexpressed AdeP transports adenine but not guanine, hypoxanthine, xanthine, uric acid or uracil . AdeP is a member of the nucleobase:cation symporter 2 (NCS2) family of transporters . adeP: adenine specific permease purP: purine permease

## Biological Role

Repressed by DNA-binding transcriptional dual regulator KdpE-phosphorylated (complex.ecocyc.CPLX0-7795). Activated by yiaU (protein.P37682).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31466|protein.P31466]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37682|protein.P37682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7795|complex.ecocyc.CPLX0-7795]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012148,ECOCYC:EG11724,GeneID:948224`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3895272-3896609:-; feature_type=gene
