---
entity_id: "gene.b2384"
entity_type: "gene"
name: "ypdE"
source_database: "NCBI RefSeq"
source_id: "gene-b2384"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2384"
  - "ypdE"
---

# ypdE

`gene.b2384`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2384`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ypdE (gene.b2384) is a gene entity. It encodes ypdE (protein.P77585). Encoded protein function: FUNCTION: Has a broad aminopeptidase activity on non-blocked peptides by progressively cleaving amino acids off the peptide substrate. Aminopeptidase activity stops at the residue before the first proline in the peptide. Cannot cleave when proline is the first N-terminal residue. {ECO:0000269|PubMed:15901689}. EcoCyc product frame: G7247-MONOMER. Genomic coordinates: 2504510-2505547. EcoCyc protein note: YpdE is a metalloaminopeptidase with broad activity on nonblocked peptides. Its is unable to cleave at Xaa-Pro or Pro-Xaa . A ypdE deletion mutant is more sensitive to kasugamycin than wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77585|protein.P77585]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007864,ECOCYC:G7247,GeneID:946848`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2504510-2505547:-; feature_type=gene
