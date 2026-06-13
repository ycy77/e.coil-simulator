---
entity_id: "gene.b2487"
entity_type: "gene"
name: "hyfG"
source_database: "NCBI RefSeq"
source_id: "gene-b2487"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2487"
  - "hyfG"
---

# hyfG

`gene.b2487`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2487`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyfG (gene.b2487) is a gene entity. It encodes hyfG (protein.P77329). Encoded protein function: FUNCTION: Possible component of hydrogenase 4. {ECO:0000305|PubMed:9387241}. EcoCyc product frame: MONOMER0-150. Genomic coordinates: 2608487-2610154. EcoCyc protein note: hyfABCDEFGHI encodes a predicted nine subunit Ni-Fe hydrogenase complex (hydrogenase 4). HyfG shows sequence similarity with the large subunit of hydrogenase 3 (HycE) and with the NuoD subunit of NADH oxidoreductase; the protein contains a predicted [Ni-Fe (CO)(CN)2] cluster

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77329|protein.P77329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008194,ECOCYC:G7304,GeneID:946964`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2608487-2610154:+; feature_type=gene
