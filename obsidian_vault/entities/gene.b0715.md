---
entity_id: "gene.b0715"
entity_type: "gene"
name: "abrB"
source_database: "NCBI RefSeq"
source_id: "gene-b0715"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0715"
  - "abrB"
---

# abrB

`gene.b0715`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0715`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abrB (gene.b0715) is a gene entity. It encodes abrB (protein.P75747). Encoded protein function: FUNCTION: Seems to be involved in the regulation of AidB. EcoCyc product frame: G6384-MONOMER. EcoCyc synonyms: ybgN. Genomic coordinates: 746723-747769. EcoCyc protein note: An abrB mutation causes an unstable phenotype with respect to anaerobic, Ada-independent expression of the aidB gene . AbrB: "aidB regulator B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75747|protein.P75747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002435,ECOCYC:G6384,GeneID:945321`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:746723-747769:-; feature_type=gene
