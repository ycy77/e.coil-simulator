---
entity_id: "gene.b3858"
entity_type: "gene"
name: "yihD"
source_database: "NCBI RefSeq"
source_id: "gene-b3858"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3858"
  - "yihD"
---

# yihD

`gene.b3858`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3858`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihD (gene.b3858) is a gene entity. It encodes yihD (protein.P0ADP9). Encoded protein function: Protein YihD EcoCyc product frame: EG11830-MONOMER. Genomic coordinates: 4042069-4042338. EcoCyc protein note: yihD is part of a functional interaction network that includes tRNA and rRNA methylation factors. A yihD mutant has elevated amount of free 30S and 50S ribosomal subunits and increased levels of translation errors .

## Biological Role

Activated by glaR (protein.P37338), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADP9|protein.P0ADP9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yihD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yihD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012599,ECOCYC:EG11830,GeneID:948348`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4042069-4042338:+; feature_type=gene
