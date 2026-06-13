---
entity_id: "gene.b4557"
entity_type: "gene"
name: "yidD"
source_database: "NCBI RefSeq"
source_id: "gene-b4557"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4557"
  - "yidD"
---

# yidD

`gene.b4557`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4557`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidD (gene.b4557) is a gene entity. It encodes yidD (protein.P0A8C8). Encoded protein function: FUNCTION: Could be involved in insertion of integral membrane proteins into the membrane. {ECO:0000255|HAMAP-Rule:MF_00386, ECO:0000269|PubMed:21803992}. EcoCyc product frame: MONOMER0-2692. Genomic coordinates: 3884816-3885073. EcoCyc protein note: yidD is cotranscribed with yidC; yidD mRNA is translated; yidD deletion strains have no discernable phenotype; YidD is inner membrane associated. YidD is required for the efficient processing of several known EG11197 "YidC"-dependent inner membrane proteins including the CyoA subunit of cytochrome bo terminal oxidase and subunit c of the ATP synthase F0 complex. YidD forms cysteine cross-links with the cytosolic domain of nascent FtsQ during in vitro translation suggesting that it may be in close proximity to nascent FtsQ during membrane insertion .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8C8|protein.P0A8C8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285078,ECOCYC:G0-10470,GeneID:1450303`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3884816-3885073:+; feature_type=gene
