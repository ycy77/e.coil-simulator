---
entity_id: "gene.b4766"
entity_type: "gene"
name: "argL"
source_database: "NCBI RefSeq"
source_id: "gene-b4766"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4766"
  - "argL"
---

# argL

`gene.b4766`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4766`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argL (gene.b4766) is a gene entity. It encodes argL (protein.P0DSE4). Encoded protein function: FUNCTION: May serve a regulatory role in expression of downstream gene argF; in an argL-argF-lacZ fusion mutation of the start codon to a stop codon in argL increases expression of beta-galactosidase. {ECO:0000269|PubMed:30837344}. EcoCyc product frame: MONOMER0-4479. Genomic coordinates: 290275-290370. EcoCyc protein note: ArgL was identified as a previously unannotated small protein; it is expressed in both exponential and stationary phase in rich media. Introduction of a stop codon into the argL ORF leads to increased expression of the downstream argF gene, suggesting a regulatory role of ArgL .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DSE4|protein.P0DSE4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-17012,GeneID:63925624`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:290275-290370:-; feature_type=gene
