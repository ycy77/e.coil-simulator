---
entity_id: "gene.b1344"
entity_type: "gene"
name: "ttcA"
source_database: "NCBI RefSeq"
source_id: "gene-b1344"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1344"
  - "ttcA"
---

# ttcA

`gene.b1344`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1344`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ttcA (gene.b1344) is a gene entity. It encodes ttcA (protein.P76055). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent 2-thiolation of cytidine in position 32 of tRNA, to form 2-thiocytidine (s(2)C32). The sulfur atoms are provided by the cysteine/cysteine desulfurase (IscS) system. {ECO:0000255|HAMAP-Rule:MF_01850, ECO:0000269|PubMed:24914049, ECO:0000305|PubMed:14729701}. EcoCyc product frame: G6675-MONOMER. EcoCyc synonyms: ydaO. Genomic coordinates: 1411013-1411948.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76055|protein.P76055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004514,ECOCYC:G6675,GeneID:948967`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1411013-1411948:-; feature_type=gene
