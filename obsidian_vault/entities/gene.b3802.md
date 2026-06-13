---
entity_id: "gene.b3802"
entity_type: "gene"
name: "hemY"
source_database: "NCBI RefSeq"
source_id: "gene-b3802"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3802"
  - "hemY"
---

# hemY

`gene.b3802`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3802`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemY (gene.b3802) is a gene entity. It encodes hemY (protein.P0ACB7). Encoded protein function: FUNCTION: Involved in a late step of protoheme IX synthesis. EcoCyc product frame: EG10434-MONOMER. Genomic coordinates: 3986686-3987882. EcoCyc protein note: HemY is predicted to be an inner membrane protein with two transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . HemY is predicted to be a bitopic inner membrane protein .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACB7|protein.P0ACB7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012417,ECOCYC:EG10434,GeneID:948311`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3986686-3987882:-; feature_type=gene
