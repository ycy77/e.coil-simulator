---
entity_id: "gene.b4547"
entity_type: "gene"
name: "ypfN"
source_database: "NCBI RefSeq"
source_id: "gene-b4547"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4547"
  - "ypfN"
---

# ypfN

`gene.b4547`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4547`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ypfN (gene.b4547) is a gene entity. It encodes ypfN (protein.Q2EET2). Encoded protein function: UPF0370 protein YpfN EcoCyc product frame: MONOMER0-2685. Genomic coordinates: 2592762-2592962. EcoCyc protein note: Overexpression of ypfN (in 'wild-type' strain MG1655 ΔhsdR) increases ampicillin resistance; deletion of ypfN increases susceptibility to ampicillin in the presence of a β-lactamase expressing plasmid but does not impact susceptibility to ampicillin in the wild-type . ypfN is highly conserved in E. coli .

## Biological Role

Activated by sutR (protein.P77626).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2EET2|protein.Q2EET2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P77626|protein.P77626]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0285068,ECOCYC:G0-10463,GeneID:1450286`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2592762-2592962:+; feature_type=gene
