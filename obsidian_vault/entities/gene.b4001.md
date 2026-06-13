---
entity_id: "gene.b4001"
entity_type: "gene"
name: "yjaH"
source_database: "NCBI RefSeq"
source_id: "gene-b4001"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4001"
  - "yjaH"
---

# yjaH

`gene.b4001`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4001`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjaH (gene.b4001) is a gene entity. It encodes yjaH (protein.P32681). Encoded protein function: Uncharacterized protein YjaH EcoCyc product frame: EG11917-MONOMER. Genomic coordinates: 4200566-4201261. EcoCyc protein note: Sequence similarity suggests that YjaH may contain β-barrel structure(s) .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32681|protein.P32681]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjaH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013079,ECOCYC:EG11917,GeneID:948508`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4200566-4201261:+; feature_type=gene
