---
entity_id: "gene.b1058"
entity_type: "gene"
name: "yceO"
source_database: "NCBI RefSeq"
source_id: "gene-b1058"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1058"
  - "yceO"
---

# yceO

`gene.b1058`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1058`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yceO (gene.b1058) is a gene entity. It encodes yceO (protein.P64442). Encoded protein function: Uncharacterized protein YceO EcoCyc product frame: G6555-MONOMER. Genomic coordinates: 1119307-1119447. EcoCyc protein note: YceO appears to be involved in biofilm formation and the acid stress response . The YceO open reading frame contains a predicted transmembrane segment . Expression of yceO increases 11-fold upon deletion of tqsA, which increases biofilm formation . YceO is expressed during exponential growth . A mutant with a deletion of yceO shows a significant decrease in biofilm formation . In growth competition experiments, a yceO deletion mutant is more sensitive to acute acid stress than the wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64442|protein.P64442]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003588,ECOCYC:G6555,GeneID:945629`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1119307-1119447:-; feature_type=gene
