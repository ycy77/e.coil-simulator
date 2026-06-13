---
entity_id: "gene.b1561"
entity_type: "gene"
name: "rem"
source_database: "NCBI RefSeq"
source_id: "gene-b1561"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1561"
  - "rem"
---

# rem

`gene.b1561`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1561`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rem (gene.b1561) is a gene entity. It encodes rem (protein.P07010). Encoded protein function: Uncharacterized protein Rem EcoCyc product frame: EG11129-MONOMER. Genomic coordinates: 1644651-1644902. EcoCyc protein note: Rem has been identified as a putative antirepressor of DicA, encoded in the cryptic prophage Qin, as it induces the derepression of dicBp, a promoter repressed by DicA .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07010|protein.P07010]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005215,ECOCYC:EG11129,GeneID:946109`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1644651-1644902:-; feature_type=gene
