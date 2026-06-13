---
entity_id: "gene.b2823"
entity_type: "gene"
name: "ppdC"
source_database: "NCBI RefSeq"
source_id: "gene-b2823"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2823"
  - "ppdC"
---

# ppdC

`gene.b2823`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2823`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppdC (gene.b2823) is a gene entity. It encodes ppdC (protein.P08372). Encoded protein function: FUNCTION: Not yet known. EcoCyc product frame: EG11154-MONOMER. EcoCyc synonyms: ygdA. Genomic coordinates: 2962441-2962764. EcoCyc protein note: PpdC is predicted to be a bitopic inner membrane protein .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08372|protein.P08372]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ppdC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009257,ECOCYC:EG11154,GeneID:945797`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2962441-2962764:-; feature_type=gene
