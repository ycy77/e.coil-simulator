---
entity_id: "gene.b3688"
entity_type: "gene"
name: "yidQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3688"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3688"
  - "yidQ"
---

# yidQ

`gene.b3688`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3688`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidQ (gene.b3688) is a gene entity. It encodes yidQ (protein.P0ADM4). Encoded protein function: Uncharacterized protein YidQ EcoCyc product frame: EG11712-MONOMER. EcoCyc synonyms: ecfI. Genomic coordinates: 3867728-3868060. EcoCyc protein note: YidQ is a protein with a possible extracytoplasmic function; transcription is regulated by RpoE (σE) . EcfI: "extracytoplasmic function I"

## Biological Role

Activated by rpoE (protein.P0AGB6), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADM4|protein.P0ADM4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yidQ; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yidQ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012063,ECOCYC:EG11712,GeneID:948199`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3867728-3868060:+; feature_type=gene
