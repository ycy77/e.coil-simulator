---
entity_id: "gene.b4082"
entity_type: "gene"
name: "mdtN"
source_database: "NCBI RefSeq"
source_id: "gene-b4082"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4082"
  - "mdtN"
---

# mdtN

`gene.b4082`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4082`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtN (gene.b4082) is a gene entity. It encodes mdtN (protein.P32716). Encoded protein function: FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride. EcoCyc product frame: EG11954-MONOMER. EcoCyc synonyms: yjcR, sdsR. Genomic coordinates: 4303078-4304109. EcoCyc protein note: MdtN is predicted to be the membrane fusion protein component of a putative multidrug efflux pump . An mdtN null mutant is more sensitive to sulfonamide antibiotics than wild type . sdsR: sulfa drug sensitivity mdtN: multi drug transporter

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32716|protein.P32716]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013373,ECOCYC:EG11954,GeneID:948598`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4303078-4304109:-; feature_type=gene
