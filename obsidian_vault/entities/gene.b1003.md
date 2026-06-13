---
entity_id: "gene.b1003"
entity_type: "gene"
name: "yccJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1003"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1003"
  - "yccJ"
---

# yccJ

`gene.b1003`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1003`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yccJ (gene.b1003) is a gene entity. It encodes yccJ (protein.P0AB14). Encoded protein function: Uncharacterized protein YccJ EcoCyc product frame: EG12703-MONOMER. Genomic coordinates: 1066864-1067091. EcoCyc protein note: Overexpression of yccJ from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Biological Role

Activated by csgD (protein.P52106).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB14|protein.P0AB14]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=yccJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003390,ECOCYC:EG12703,GeneID:948930`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1066864-1067091:-; feature_type=gene
