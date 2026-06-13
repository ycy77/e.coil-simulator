---
entity_id: "gene.b1100"
entity_type: "gene"
name: "ycfH"
source_database: "NCBI RefSeq"
source_id: "gene-b1100"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1100"
  - "ycfH"
---

# ycfH

`gene.b1100`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1100`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycfH (gene.b1100) is a gene entity. It encodes ycfH (protein.P0AFQ7). Encoded protein function: FUNCTION: Has D-tyrosyl-tRNA deacylase activity in vitro. {ECO:0000269|PubMed:19332551}. EcoCyc product frame: EG12303-MONOMER. Genomic coordinates: 1156777-1157574. EcoCyc protein note: YcfH and YjjV have similarity to the TatD DNase . A tatD ycfH yjjV triple mutant does not exhibit defects in the export of Tat pathway substrates, suggesting that they are not required for the Sec-independent protein export system in which TatA, TatB, and TatC participate . A ycfH deletion mutant is more sensitive to kasugamycin than wild type . An in-frame substitution of the holB gene with a kanamycin resistance gene has no polar effect on ycfH .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFQ7|protein.P0AFQ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003719,ECOCYC:EG12303,GeneID:945656`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1156777-1157574:+; feature_type=gene
