---
entity_id: "gene.b0983"
entity_type: "gene"
name: "gfcE"
source_database: "NCBI RefSeq"
source_id: "gene-b0983"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0983"
  - "gfcE"
---

# gfcE

`gene.b0983`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0983`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gfcE (gene.b0983) is a gene entity. It encodes gfcE (protein.P0A932). Encoded protein function: FUNCTION: May be involved in polysaccharide transport. EcoCyc product frame: G6504-MONOMER. EcoCyc synonyms: yccZ. Genomic coordinates: 1044664-1045803. EcoCyc protein note: GfcE is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . This operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site .

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A932|protein.P0A932]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003317,ECOCYC:G6504,GeneID:945586`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1044664-1045803:-; feature_type=gene
