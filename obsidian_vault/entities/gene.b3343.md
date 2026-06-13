---
entity_id: "gene.b3343"
entity_type: "gene"
name: "tusB"
source_database: "NCBI RefSeq"
source_id: "gene-b3343"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3343"
  - "tusB"
---

# tusB

`gene.b3343`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3343`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tusB (gene.b3343) is a gene entity. It encodes tusB (protein.P45530). Encoded protein function: FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. {ECO:0000269|PubMed:16387657}. EcoCyc product frame: G7712-MONOMER. EcoCyc synonyms: yheL. Genomic coordinates: 3474678-3474965. EcoCyc protein note: A tusB deletion mutant lacks the 2-thio modification of mnm5s2U in tRNA and has a severe growth defect . TusB: "tRNA 2-thiouridine synthesizing protein"

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45530|protein.P45530]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010922,ECOCYC:G7712,GeneID:947844`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3474678-3474965:-; feature_type=gene
