---
entity_id: "gene.b0290"
entity_type: "gene"
name: "ecpD"
source_database: "NCBI RefSeq"
source_id: "gene-b0290"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0290"
  - "ecpD"
---

# ecpD

`gene.b0290`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0290`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecpD (gene.b0290) is a gene entity. It encodes ecpD (protein.P77694). Encoded protein function: FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Tip pilus adhesin, which is required for assembly of EcpA into fibers (By similarity). {ECO:0000250}. EcoCyc product frame: G6161-MONOMER. EcoCyc synonyms: yagW, matE. Genomic coordinates: 305174-306817. EcoCyc protein note: EcpD (formerly MatE) is a novel polymerized tip adhesin of the E.coli common pilus (ECP) that is expressed in pathogenic E. coli strains at low temperatures . ECP is not expressed in E. coli K-12 . Overexpression of the cloned E. coli K-12 MG1655 ecpABCDE genes in wild type E. coli K12 MG1655 results in ECP expression at 20oC and 37oC and biofilm formation at 20oC indicating that the genes are functional in E. coli MG1655 but are not expressed . Sequence similarity suggests that it may contain β-barrel structure(s) . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ecpABCDE; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77694|protein.P77694]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001002,ECOCYC:G6161,GeneID:947349`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:305174-306817:-; feature_type=gene
