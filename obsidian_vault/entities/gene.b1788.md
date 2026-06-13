---
entity_id: "gene.b1788"
entity_type: "gene"
name: "yoaI"
source_database: "NCBI RefSeq"
source_id: "gene-b1788"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1788"
  - "yoaI"
---

# yoaI

`gene.b1788`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1788`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaI (gene.b1788) is a gene entity. It encodes yoaI (protein.P76239). Encoded protein function: Uncharacterized protein YoaI EcoCyc product frame: G6974-MONOMER. Genomic coordinates: 1874078-1874182. EcoCyc protein note: Expression of the predicted small protein YoaI was not detected under the conditions used by . yoaI may be a member of the PhoB regulon in E. coli O157:H7 .

## Biological Role

Activated by phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76239|protein.P76239]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005947,ECOCYC:G6974,GeneID:946294`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1874078-1874182:-; feature_type=gene
