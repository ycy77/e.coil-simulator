---
entity_id: "gene.b1959"
entity_type: "gene"
name: "yedA"
source_database: "NCBI RefSeq"
source_id: "gene-b1959"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1959"
  - "yedA"
---

# yedA

`gene.b1959`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1959`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yedA (gene.b1959) is a gene entity. It encodes yedA (protein.P0AA70). Encoded protein function: Uncharacterized inner membrane transporter YedA EcoCyc product frame: EG11141-MONOMER. Genomic coordinates: 2029539-2030459. EcoCyc protein note: In the Transporter Classification Database, YedA is a member of the Drug/Metabolite Exporter (DME) family within the Drug/Metabolite Transporter (DMT) superfamily . Overexpression of yedA from a plasmid confers resistance to the toxic chemical, bromoacetate .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA70|protein.P0AA70]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006505,ECOCYC:EG11141,GeneID:946461`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2029539-2030459:+; feature_type=gene
