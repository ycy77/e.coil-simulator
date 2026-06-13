---
entity_id: "gene.b0859"
entity_type: "gene"
name: "rlmC"
source_database: "NCBI RefSeq"
source_id: "gene-b0859"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0859"
  - "rlmC"
---

# rlmC

`gene.b0859`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0859`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmC (gene.b0859) is a gene entity. It encodes rlmC (protein.P75817). Encoded protein function: FUNCTION: Catalyzes the formation of 5-methyl-uridine at position 747 (m5U747) in 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01012, ECO:0000269|PubMed:12907714}. EcoCyc product frame: G6449-MONOMER. EcoCyc synonyms: ybjF, rumB. Genomic coordinates: 898518-899645. EcoCyc protein note: RlmC is the methyltransferase responsible for methylation of 23S rRNA at the C5 position of the U747 nucleotide . An rlmC mutant shows a specific defect in methylation of position U747 in 23S rRNA . RumB: RNA uridine methyltransferase

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75817|protein.P75817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002924,ECOCYC:G6449,GeneID:947260`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:898518-899645:+; feature_type=gene
