---
entity_id: "gene.b0985"
entity_type: "gene"
name: "gfcC"
source_database: "NCBI RefSeq"
source_id: "gene-b0985"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0985"
  - "gfcC"
---

# gfcC

`gene.b0985`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0985`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gfcC (gene.b0985) is a gene entity. It encodes gfcC (protein.P75883). Encoded protein function: Uncharacterized protein GfcC (Group 4 capsule protein C homolog) EcoCyc product frame: G6506-MONOMER. EcoCyc synonyms: ymcB. Genomic coordinates: 1047945-1048691. EcoCyc protein note: The operon encoding YmcD, YmcC, YmcB, YmcA, YzzZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . This operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site . A ΔgfcC knockout mutant (from the Keio collection) shows enhanced secretion of the extracellular protein EG11807-MONOMER "YebF" and of YebF fusion proteins; a ΔgfcC strain shows no signs of envelope instability .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75883|protein.P75883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003321,ECOCYC:G6506,GeneID:944978`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1047945-1048691:-; feature_type=gene
