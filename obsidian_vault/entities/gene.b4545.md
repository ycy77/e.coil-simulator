---
entity_id: "gene.b4545"
entity_type: "gene"
name: "ypdJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4545"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4545"
  - "ypdJ"
---

# ypdJ

`gene.b4545`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4545`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ypdJ (gene.b4545) is a gene entity. It encodes ypdJ (protein.Q2EET0). Encoded protein function: FUNCTION: May be involved in H(2) production during fermentative growth. {ECO:0000269|PubMed:24025676}. EcoCyc product frame: MONOMER0-2683. Genomic coordinates: 2476094-2476234. EcoCyc protein note: A ypdJ null mutant obtained from the KEIO collection was reported to produce less hydrogen than wild type under fermentation conditions. (Note that the KEIO library contains a mixture of strains for this well location.) A ypdJ expression clone from the ASKA library does not complement the phenotype .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2EET0|protein.Q2EET0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285066,ECOCYC:G0-10461,GeneID:1450283`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2476094-2476234:+; feature_type=gene
