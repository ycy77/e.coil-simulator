---
entity_id: "gene.b0292"
entity_type: "gene"
name: "ecpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0292"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0292"
  - "ecpB"
---

# ecpB

`gene.b0292`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0292`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecpB (gene.b0292) is a gene entity. It encodes ecpB (protein.P77188). Encoded protein function: FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition (By similarity). {ECO:0000250}. EcoCyc product frame: G6163-MONOMER. EcoCyc synonyms: yagY, matC. Genomic coordinates: 309358-310026. EcoCyc protein note: EcpB (formerly MatC) is a predicted E. coli common pilus (ECP) chaperone that is expressed in pathogenic E. coli strains at low temperatures but is not expressed in E. coli K-12 . Overexpression of the cloned E. coli K-12 MG1655 ecpABCDE genes in wild type E. coli K-12 MG1655 results in ECP expression at 20°C and 37°C and biofilm formation at 20°C indicating that the genes are functional in E. coli MG1655 but are not expressed . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ecpABCDE; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised MatC: "meningitis associated and temperature regulated fimbria"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77188|protein.P77188]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001007,ECOCYC:G6163,GeneID:948806`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:309358-310026:-; feature_type=gene
