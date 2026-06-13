---
entity_id: "gene.b0986"
entity_type: "gene"
name: "gfcB"
source_database: "NCBI RefSeq"
source_id: "gene-b0986"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0986"
  - "gfcB"
---

# gfcB

`gene.b0986`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0986`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gfcB (gene.b0986) is a gene entity. It encodes gfcB (protein.P75884). Encoded protein function: Uncharacterized lipoprotein GfcB (Group 4 capsule protein B homolog) EcoCyc product frame: G6507-MONOMER. EcoCyc synonyms: ymcC. Genomic coordinates: 1048688-1049332. EcoCyc protein note: Sequence similarity suggests that YmcC may be a lipoprotein and/or an outer membrane porin . GfcB is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . This operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75884|protein.P75884]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003323,ECOCYC:G6507,GeneID:949118`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1048688-1049332:-; feature_type=gene
