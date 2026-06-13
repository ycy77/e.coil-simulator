---
entity_id: "gene.b0824"
entity_type: "gene"
name: "ybiY"
source_database: "NCBI RefSeq"
source_id: "gene-b0824"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0824"
  - "ybiY"
---

# ybiY

`gene.b0824`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0824`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiY (gene.b0824) is a gene entity. It encodes ybiY (protein.P75794). Encoded protein function: FUNCTION: Activation of pyruvate formate-lyase 2 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000250}. EcoCyc product frame: G6427-MONOMER. EcoCyc synonyms: pflE. Genomic coordinates: 862612-863511. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 23, 2018. However, based on its similarity to PFLACTENZ-MONOMER (EG10028) it has been annotated as a putative pyruvate formate-lyase activating enzyme.

## Biological Role

Activated by yciT (protein.P76034).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75794|protein.P75794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P76034|protein.P76034]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002812,ECOCYC:G6427,GeneID:945445`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:862612-863511:-; feature_type=gene
