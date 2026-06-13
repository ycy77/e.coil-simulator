---
entity_id: "gene.b0293"
entity_type: "gene"
name: "ecpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0293"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0293"
  - "ecpA"
---

# ecpA

`gene.b0293`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0293`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ecpA (gene.b0293) is a gene entity. It encodes ecpA (protein.P0AAA3). Encoded protein function: FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Major subunit of the fimbria (By similarity). {ECO:0000250}. EcoCyc product frame: G6164-MONOMER. EcoCyc synonyms: yagZ, matB. Genomic coordinates: 310084-310671. EcoCyc protein note: EcpA (formerly MatB) is the major structural component of the E.coli common pilus (ECP) that is expressed in pathogenic E. coli strains at low temperatures . ECP are not expressed in E. coli K-12 . ecpA from E.coli K-12 MG1655 has 97.8% sequence identity with ecpA from the pathogenic isolate O18acK1H7 . Overexpression of the cloned E. coli K-12 MG1655 ecpABCDE genes in wild type E. coli K12 MG1655 results in ECP expression at 20oC and 37oC and biofilm formation at 20oC indicating that the genes are functional in E. coli MG1655 but are not expressed . ecpA (matB) is highly conserved in the genomes of E. coli strains, and most pathogenic strains of E. coli produce an ECP encoded by ecpA . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ecpABCDE; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised EcpA: "E...

## Biological Role

Activated by ecpR (protein.P71301).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAA3|protein.P0AAA3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=ecpA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001009,ECOCYC:G6164,GeneID:948759`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:310084-310671:-; feature_type=gene
