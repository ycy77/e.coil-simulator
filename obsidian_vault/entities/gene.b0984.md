---
entity_id: "gene.b0984"
entity_type: "gene"
name: "gfcD"
source_database: "NCBI RefSeq"
source_id: "gene-b0984"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0984"
  - "gfcD"
---

# gfcD

`gene.b0984`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0984`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gfcD (gene.b0984) is a gene entity. It encodes gfcD (protein.P75882). Encoded protein function: Uncharacterized lipoprotein GfcD (Group 4 capsule protein D homolog) EcoCyc product frame: G6505-MONOMER. EcoCyc synonyms: ymcA. Genomic coordinates: 1045849-1047945. EcoCyc protein note: The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . This operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75882|protein.P75882]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003319,ECOCYC:G6505,GeneID:945588`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1045849-1047945:-; feature_type=gene
