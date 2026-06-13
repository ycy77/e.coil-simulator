---
entity_id: "gene.b0330"
entity_type: "gene"
name: "prpR"
source_database: "NCBI RefSeq"
source_id: "gene-b0330"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0330"
  - "prpR"
---

# prpR

`gene.b0330`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0330`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prpR (gene.b0330) is a gene entity. It encodes prpR (protein.P77743). Encoded protein function: FUNCTION: Involved in the transcriptional regulation of the propionate catabolism operon. EcoCyc product frame: G6195-MONOMER. EcoCyc synonyms: yahP. Genomic coordinates: 346857-348443.

## Biological Role

Repressed by phoB (protein.P0AFJ5), ascG (protein.P24242). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77743|protein.P77743]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=prpR; function=+
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=prpR; function=-
- `represses` <-- [[protein.P24242|protein.P24242]] `RegulonDB` `C` - regulator=AscG; target=prpR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001133,ECOCYC:G6195,GeneID:944987`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:346857-348443:-; feature_type=gene
