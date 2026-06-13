---
entity_id: "gene.b1140"
entity_type: "gene"
name: "intE"
source_database: "NCBI RefSeq"
source_id: "gene-b1140"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1140"
  - "intE"
---

# intE

`gene.b1140`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1140`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

intE (gene.b1140) is a gene entity. It encodes intE (protein.P75969). Encoded protein function: FUNCTION: Integrase from the cryptic lambdoid prophage e14. Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. EcoCyc product frame: EG12370-MONOMER. EcoCyc synonyms: int(Lambda), ycfI. Genomic coordinates: 1199679-1200806. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 18, 2016.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75969|protein.P75969]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003836,ECOCYC:EG12370,GeneID:948034`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1199679-1200806:-; feature_type=gene
