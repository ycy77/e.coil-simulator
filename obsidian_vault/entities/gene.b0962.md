---
entity_id: "gene.b0962"
entity_type: "gene"
name: "helD"
source_database: "NCBI RefSeq"
source_id: "gene-b0962"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0962"
  - "helD"
---

# helD

`gene.b0962`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0962`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

helD (gene.b0962) is a gene entity. It encodes helD (protein.P15038). Encoded protein function: FUNCTION: Helicase IV catalyzes the unwinding of duplex DNA in the 3' to 5' direction with respect to the bound single strand in a reaction that is dependent upon the hydrolysis of (d)ATP. {ECO:0000269|PubMed:2822720}. EcoCyc product frame: EG10426-MONOMER. EcoCyc synonyms: srjB. Genomic coordinates: 1024471-1026525. EcoCyc protein note: DNA helicase IV (HelD) is an ATP-dependent 3'->5' DNA helicase belonging to the helicase superfamily I . HelD appears to interact with ssDNA by a distributed mechanism; addition of SSB stimulates the DNA unwinding reaction two-fold . The presence of a protein bound to dsDNA substantially inhibits the helicase activity of HelD . The predicted ATP binding site of HelD was investigated by site-directed mutagenesis. Mutants in the conserved Q201 and Y502 residues lead to loss of ATPase activity; the S224H and S224M mutants showed unaffected ATPase and DNA binding activities, but severely reduced helicase activity . There appears to be functional overlap between RecQ helicase, helicase II, and helicase IV . Analysis of combinations of mutants in genes of the RecF pathway revealed synergistic interactions between helD and recF/recO in recombinational repair...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15038|protein.P15038]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003257,ECOCYC:EG10426,GeneID:946227`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1024471-1026525:+; feature_type=gene
