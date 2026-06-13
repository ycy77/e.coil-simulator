---
entity_id: "gene.b0289"
entity_type: "gene"
name: "ecpE"
source_database: "NCBI RefSeq"
source_id: "gene-b0289"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0289"
  - "ecpE"
---

# ecpE

`gene.b0289`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0289`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecpE (gene.b0289) is a gene entity. It encodes ecpE (protein.P77263). Encoded protein function: FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition (By similarity). {ECO:0000250}. EcoCyc product frame: G6160-MONOMER. EcoCyc synonyms: yagV, matF. Genomic coordinates: 304495-305205. EcoCyc protein note: EcpE (formerly MatF) is a predicted E. coli common pilus (ECP) chaperone that is expressed in pathogenic E. coli strains at low temperatures but is not expressed in E. coli K-12 . Overexpression of the cloned E. coli K-12 MG1655 ecpABCDE genes in wild type E. coli K12 MG1655 results in ECP expression at 20oC and 37oC and biofilm formation at 20oC indicating that the genes are functional in E. coli MG1655 but are not expressed . Sequence similarity suggests that EcpE may contain β-barrel structure(s) . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ecpABCDE; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised Mat: "meningitis associated and temperature regulated fimbria"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77263|protein.P77263]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001000,ECOCYC:G6160,GeneID:946631`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:304495-305205:-; feature_type=gene
