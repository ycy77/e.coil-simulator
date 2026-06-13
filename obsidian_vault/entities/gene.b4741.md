---
entity_id: "gene.b4741"
entity_type: "gene"
name: "ymiC"
source_database: "NCBI RefSeq"
source_id: "gene-b4741"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4741"
  - "ymiC"
---

# ymiC

`gene.b4741`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4741`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymiC (gene.b4741) is a gene entity. It encodes ymiC (protein.P0DPO1). Encoded protein function: Protein YmiC EcoCyc product frame: MONOMER0-4418. Genomic coordinates: 1335572-1335667. EcoCyc protein note: YmiC was identified as a previously unannotated small protein; its expression is higher during stationary phase than during exponential phase .

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPO1|protein.P0DPO1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ymiC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ymiC; function=+

## External IDs

- `Dbxref:ECOCYC:G0-16736,GeneID:38094953`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1335572-1335667:+; feature_type=gene
