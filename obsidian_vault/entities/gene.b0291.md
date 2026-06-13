---
entity_id: "gene.b0291"
entity_type: "gene"
name: "ecpC"
source_database: "NCBI RefSeq"
source_id: "gene-b0291"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0291"
  - "ecpC"
---

# ecpC

`gene.b0291`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0291`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecpC (gene.b0291) is a gene entity. It encodes ecpC (protein.P77802). Encoded protein function: FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition (By similarity). {ECO:0000250}. EcoCyc product frame: G6162-MONOMER. EcoCyc synonyms: yagX, matD. Genomic coordinates: 306807-309332. EcoCyc protein note: EcpC (formerly MatD) is a predicted outer membrane protein associated with E. coli common pilus (ECP) formation in pathogenic E. coli strains . ecpC may be cryptic in E. coli K-12. Overexpression of the cloned E. coli K-12 MG1655 ecpABCDE genes in wild type E. coli K12 MG1655 results in ECP expression at 20oC and 37oC and biofilm formation at 20oC indicating that the genes are functional in E. coli MG1655 but are not expressed . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ecpABCDE; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised Mat: "meningitis associated and temperature regulated fimbria"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77802|protein.P77802]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001005,ECOCYC:G6162,GeneID:947606`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:306807-309332:-; feature_type=gene
