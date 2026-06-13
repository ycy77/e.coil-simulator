---
entity_id: "gene.b1758"
entity_type: "gene"
name: "ynjF"
source_database: "NCBI RefSeq"
source_id: "gene-b1758"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1758"
  - "ynjF"
---

# ynjF

`gene.b1758`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1758`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynjF (gene.b1758) is a gene entity. It encodes ynjF (protein.P76226). Encoded protein function: Inner membrane protein YnjF EcoCyc product frame: G6953-MONOMER. Genomic coordinates: 1840783-1841403. EcoCyc protein note: YnjF is predicted to be an inner membrane protein with 5 transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . A ΔynjF mutant has aggravating genetic interactions with genes involved in DNA recomination .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76226|protein.P76226]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynjF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005850,ECOCYC:G6953,GeneID:946221`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1840783-1841403:-; feature_type=gene
