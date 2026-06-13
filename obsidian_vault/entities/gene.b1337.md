---
entity_id: "gene.b1337"
entity_type: "gene"
name: "abgB"
source_database: "NCBI RefSeq"
source_id: "gene-b1337"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1337"
  - "abgB"
---

# abgB

`gene.b1337`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1337`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abgB (gene.b1337) is a gene entity. It encodes abgB (protein.P76052). Encoded protein function: FUNCTION: Component of the p-aminobenzoyl-glutamate hydrolase multicomponent enzyme system which catalyzes the cleavage of p-aminobenzoyl-glutamate (PABA-GLU) to form p-aminobenzoate (PABA) and glutamate. AbgAB does not degrade dipeptides and the physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}. EcoCyc product frame: G6669-MONOMER. EcoCyc synonyms: ydaI. Genomic coordinates: 1401810-1403255. EcoCyc protein note: AbgB: "p-aminobenzoyl-glutamate utilization"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76052|protein.P76052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004491,ECOCYC:G6669,GeneID:945950`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1401810-1403255:-; feature_type=gene
