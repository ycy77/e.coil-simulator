---
entity_id: "gene.b0710"
entity_type: "gene"
name: "ybgI"
source_database: "NCBI RefSeq"
source_id: "gene-b0710"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0710"
  - "ybgI"
---

# ybgI

`gene.b0710`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0710`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgI (gene.b0710) is a gene entity. It encodes ybgI (protein.P0AFP6). Encoded protein function: FUNCTION: Provides significant protection from radiation damage and may be involved in the degradation of radiation-damaged nucleotides. {ECO:0000269|PubMed:25049088}. EcoCyc product frame: G6379-MONOMER. Genomic coordinates: 742827-743570. EcoCyc protein note: YbgI is proposed to be a hydrolase-oxidase. YbgI has structural similarity to proteins with DNA-related functions . A recent study of the DUF34 protein family suggests that the proteins may function as metal ion insertases, chaperones, or metallocofactor maturases rather than GTP cyclohydrolases . YbgI localizes to the cell poles . Crystal structures of YbgI have been solved at 2.2 Å resolution. YbgI forms a toroidal complex comprising three sets of homodimers, with metal ions (two per monomer) coordinated within the ring . ybgI insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A ybgI deletion mutant has a substantial decrease in IR survival , but does not appear to have increased sensitivity to UV damage; it is more sensitive to fosfomycin, carbenicillin, vancomycin, and amoxicillin...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFP6|protein.P0AFP6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002424,ECOCYC:G6379,GeneID:945824`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:742827-743570:+; feature_type=gene
