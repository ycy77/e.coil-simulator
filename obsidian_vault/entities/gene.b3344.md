---
entity_id: "gene.b3344"
entity_type: "gene"
name: "tusC"
source_database: "NCBI RefSeq"
source_id: "gene-b3344"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3344"
  - "tusC"
---

# tusC

`gene.b3344`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3344`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tusC (gene.b3344) is a gene entity. It encodes tusC (protein.P45531). Encoded protein function: FUNCTION: Part of a sulfur-relay system required for 2-thiolation of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at tRNA wobble positions. {ECO:0000269|PubMed:16387657}. EcoCyc product frame: G7713-MONOMER. EcoCyc synonyms: yheM. Genomic coordinates: 3474973-3475332. EcoCyc protein note: A tusC deletion mutant lacks the 2-thio modification of mnm5s2U in tRNA and has a severe growth defect . TusC: "tRNA 2-thiouridine synthesizing protein"

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45531|protein.P45531]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010928,ECOCYC:G7713,GeneID:947853`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3474973-3475332:-; feature_type=gene
