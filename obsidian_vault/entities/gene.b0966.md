---
entity_id: "gene.b0966"
entity_type: "gene"
name: "hspQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0966"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0966"
  - "hspQ"
---

# hspQ

`gene.b0966`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0966`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hspQ (gene.b0966) is a gene entity. It encodes hspQ (protein.P0AB20). Encoded protein function: FUNCTION: Involved in the degradation of certain denaturated proteins, including DnaA, during heat shock stress. EcoCyc product frame: G6500-MONOMER. EcoCyc synonyms: yccV. Genomic coordinates: 1028404-1028721. EcoCyc protein note: HspQ binds to hemimethylated DNA at oriC . The HspQ protein of Yersinia pestis functions as a specificity-enhancing factor for the Lon protease . In Salmonella enterica, HspQ switches from activating Lon to binding and inhibiting ClpS-dependent proteolysis upon acetylation . The HspQ protein appeared to form dimers and higher order multimers in solution ; in a crystal structure, HspQ forms a homotrimer . An hspQ mutant suppresses the temperature sensitivity of the dnaA508 and dnaA167 alleles ; reports differ on whether or not an hspQ mutant also suppresses the temperature sensitivity of the dnaA46 allele. Overexpression of HspQ exacerbates the growth defect of the dnaA508 and dnaA167 alleles . Overexpression of the D25A, D27A, W51A, H53A, or Y67A mutants of HspQ exacerbate the dnaA508 growth defect to a lesser degree than wild type; thus, these residues appear to be involved in the in vivo function of HspQ . HspQ protein stimulates the degradation of the DnaA508 mutant protein, but not of DnaA46 . In an hspQ mutant, levels of DnaA appear to be increased...

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB20|protein.P0AB20]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003269,ECOCYC:G6500,GeneID:945578`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1028404-1028721:-; feature_type=gene
