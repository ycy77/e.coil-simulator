---
entity_id: "gene.b2968"
entity_type: "gene"
name: "yghD"
source_database: "NCBI RefSeq"
source_id: "gene-b2968"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2968"
  - "yghD"
---

# yghD

`gene.b2968`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2968`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghD (gene.b2968) is a gene entity. It encodes yghD (protein.Q46832). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. {ECO:0000305}. EcoCyc product frame: G7535-MONOMER. EcoCyc synonyms: ecfC. Genomic coordinates: 3110590-3111126. EcoCyc protein note: YghD has homology to the GspM Type II secretion system protein from enterotoxigenic E. coli strain H10407 . In pathogenic (and some commensal) E. coli strains, GspM functions as part of a virulence associated type II secretion pathway - known as T2SSβ or T2SS H10407; examination of T2SSΒ encoding loci in various strains indicates that E. coli K-12 carries remnants of the pathway but has experienced a deletion which removed a large internal region of the T2SSβ encoding operon . YghD is predicted to be a bitopic inner membrane protein . Ecf: "extracytoplasmic function"

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46832|protein.Q46832]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009740,ECOCYC:G7535,GeneID:947025`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3110590-3111126:-; feature_type=gene
