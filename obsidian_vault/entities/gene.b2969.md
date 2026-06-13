---
entity_id: "gene.b2969"
entity_type: "gene"
name: "yghE"
source_database: "NCBI RefSeq"
source_id: "gene-b2969"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2969"
  - "yghE"
---

# yghE

`gene.b2969`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2969`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghE (gene.b2969) is a gene entity. It encodes yghE (protein.Q46833). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. {ECO:0000305}. EcoCyc product frame: G7536-MONOMER. EcoCyc synonyms: ecfB. Genomic coordinates: 3111128-3111988. EcoCyc protein note: YghE has homology to the GspL Type II secretion system protein from enterotoxigenic E. coli strain H10407 . In pathogenic (and some commensal) E. coli strains, GspL functions as part of a virulence associated type II secretion pathway - known as T2SSβ or T2SS H10407; examination of T2SSβ encoding loci in various strains indicates that E. coli K-12 carries remnants of the pathway but has experienced a deletion which removed a large internal region of the T2SSβ encoding operon including an N-terminal portion of yghE . YghE is predicted to be a bitopic inner membrane protein . yghE is expressed during exponential phase in rich medium . Ecf: "extracytoplasmic function"

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46833|protein.Q46833]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009742,ECOCYC:G7536,GeneID:945897`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3111128-3111988:-; feature_type=gene
