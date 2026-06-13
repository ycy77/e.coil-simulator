---
entity_id: "gene.b2100"
entity_type: "gene"
name: "yegV"
source_database: "NCBI RefSeq"
source_id: "gene-b2100"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2100"
  - "yegV"
---

# yegV

`gene.b2100`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2100`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegV (gene.b2100) is a gene entity. It encodes yegV (protein.P76419). Encoded protein function: Uncharacterized sugar kinase YegV (EC 2.7.1.-) EcoCyc product frame: G7132-MONOMER. Genomic coordinates: 2181096-2182061. EcoCyc protein note: This uncharacterized enzyme was found to interact with the PGMI-MONOMER enzyme in glycolysis in a large assessment of protein-protein interactions (PPIs) . The products of yegT, yegU, and yegV are implicated in glycogen accumulation .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76419|protein.P76419]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006950,ECOCYC:G7132,GeneID:946637`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2181096-2182061:+; feature_type=gene
