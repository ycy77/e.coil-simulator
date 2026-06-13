---
entity_id: "gene.b0281"
entity_type: "gene"
name: "intF"
source_database: "NCBI RefSeq"
source_id: "gene-b0281"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0281"
  - "intF"
---

# intF

`gene.b0281`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0281`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

intF (gene.b0281) is a gene entity. It encodes intF (protein.P71298). Encoded protein function: FUNCTION: Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. EcoCyc product frame: G6152-MONOMER. EcoCyc synonyms: yagO. Genomic coordinates: 295696-297096. EcoCyc protein note: No information about this protein was found by a literature search conducted on January 18, 2007.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71298|protein.P71298]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000979,ECOCYC:G6152,GeneID:947351`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:295696-297096:-; feature_type=gene
