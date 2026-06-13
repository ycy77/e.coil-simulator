---
entity_id: "gene.b1731"
entity_type: "gene"
name: "cedA"
source_database: "NCBI RefSeq"
source_id: "gene-b1731"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1731"
  - "cedA"
---

# cedA

`gene.b1731`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1731`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cedA (gene.b1731) is a gene entity. It encodes cedA (protein.P0AE60). Encoded protein function: FUNCTION: Activates the cell division inhibited by chromosomal DNA over-replication. {ECO:0000269|PubMed:9278503}. EcoCyc product frame: G6936-MONOMER. EcoCyc synonyms: ydjP. Genomic coordinates: 1813421-1813663. EcoCyc protein note: CedA appears to be involved in the regulation of cell division in a wild-type or dnaA mutant strain . Multicopy overproduction of CedA suppresses the cold sensitivity of a dnaAcos mutant . Multicopy overproduction causes increased cell division in a dnaAcos mutant background, but does not suppress the DNA over-replication phenotype of this strain, suggesting that excessive DNA replication may trigger a cell division checkpoint and that overproduction of CedA bypasses the arrest . The N-terminal domain of CedA is not required for suppression; however, an E32A mutation eliminates the suppressor activity . The solution structure of CedA has been determined by NMR spectroscopy, showing similarity of CedA to DNA binding proteins. CedA has four anti-parallel β-strands, an α-helix, and a large N-terminal tail . CedA has been shown through gel-shift experiments and NMR chemical shift perturbations to bind double-stranded DNA. The β-sheet mediates this interaction . A consensus binding site sequence was identified by SELEX...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE60|protein.P0AE60]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005776,ECOCYC:G6936,GeneID:946235`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1813421-1813663:-; feature_type=gene
