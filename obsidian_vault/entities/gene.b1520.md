---
entity_id: "gene.b1520"
entity_type: "gene"
name: "yneE"
source_database: "NCBI RefSeq"
source_id: "gene-b1520"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1520"
  - "yneE"
---

# yneE

`gene.b1520`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1520`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yneE (gene.b1520) is a gene entity. It encodes yneE (protein.P76146). Encoded protein function: Voltage-dependent anion channel-forming protein YneE EcoCyc product frame: G6807-MONOMER. Genomic coordinates: 1608108-1609022. EcoCyc protein note: A yneE knockout mutant (from the Keio collection) exhibits strongly repressed swarming motility but shows no significant defect in swimming motility . yneE expression is reduced 3.5-fold in a luxS deleted strain (W3110 ΔluxS::Kan) compared to wild type (LB medium, early stationary phase) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76146|protein.P76146]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005072,ECOCYC:G6807,GeneID:946188`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1608108-1609022:-; feature_type=gene
