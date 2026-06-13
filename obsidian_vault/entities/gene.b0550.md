---
entity_id: "gene.b0550"
entity_type: "gene"
name: "rusA"
source_database: "NCBI RefSeq"
source_id: "gene-b0550"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0550"
  - "rusA"
---

# rusA

`gene.b0550`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0550`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rusA (gene.b0550) is a gene entity. It encodes rusA (protein.P0AG74). Encoded protein function: FUNCTION: Endonuclease that resolves Holliday junction intermediates made during homologous genetic recombination and DNA repair. Exhibits sequence and structure-selective cleavage of four-way DNA junctions, where it introduces symmetrical nicks in two strands of the same polarity at the 5' side of CC dinucleotides. Corrects the defects in genetic recombination and DNA repair associated with inactivation of ruvAB or ruvC. EcoCyc product frame: G6306-MONOMER. EcoCyc synonyms: ybcP, rus. Genomic coordinates: 573371-573733.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG74|protein.P0AG74]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001880,ECOCYC:G6306,GeneID:945174`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:573371-573733:+; feature_type=gene
