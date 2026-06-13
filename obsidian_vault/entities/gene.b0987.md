---
entity_id: "gene.b0987"
entity_type: "gene"
name: "gfcA"
source_database: "NCBI RefSeq"
source_id: "gene-b0987"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0987"
  - "gfcA"
---

# gfcA

`gene.b0987`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0987`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gfcA (gene.b0987) is a gene entity. It encodes gfcA (protein.P75885). Encoded protein function: Threonine-rich inner membrane protein GfcA (Group 4 capsule protein A homolog) EcoCyc product frame: G6508-MONOMER. EcoCyc synonyms: ymcD. Genomic coordinates: 1049439-1049744. EcoCyc protein note: The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . This operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site . YmcD has one predicted transmembrane domain. The C terminus of the protein is located in the periplasm .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75885|protein.P75885]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gfcA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003325,ECOCYC:G6508,GeneID:945029`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1049439-1049744:-; feature_type=gene
