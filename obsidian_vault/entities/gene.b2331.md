---
entity_id: "gene.b2331"
entity_type: "gene"
name: "smrB"
source_database: "NCBI RefSeq"
source_id: "gene-b2331"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2331"
  - "smrB"
---

# smrB

`gene.b2331`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2331`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

smrB (gene.b2331) is a gene entity. It encodes smrB (protein.P0A8B2). Encoded protein function: FUNCTION: Acts as a ribosome collision sensor (PubMed:35264790). Detects stalled/collided disomes (pairs of ribosomes where the leading ribosome is stalled and a second ribosome has collided with it) and endonucleolytically cleaves mRNA at the 5' boundary of the stalled ribosome (PubMed:35264790). Stalled/collided disomes form a new interface (primarily via the 30S subunits) that binds SmrB (PubMed:35264790). Cleaved mRNA becomes available for tmRNA ligation, leading to ribosomal subunit dissociation and rescue of stalled ribosomes (PubMed:35264790). {ECO:0000255|HAMAP-Rule:MF_01042, ECO:0000269|PubMed:35264790}. EcoCyc product frame: G7202-MONOMER. EcoCyc synonyms: yfcN. Genomic coordinates: 2448606-2449157. EcoCyc protein note: Ribosome rescue factor SmrB recognizes and acts on collided ribosomes; SmrB cleaves mRNAs upstream of stalled ribosomes and triggers SSRA-RNA-mediated ribosome rescue . smrB insertion mutations allow ribosomes to translate through a strong stalling motif; ΔsmrB cells are hypersensitive to erythromycin, an antibiotic that stalls elongating ribosomes at specific sequences . SmrB contains a small mutS-related (SMR) domain with motifs implicated in catalysis and RNA binding...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8B2|protein.P0A8B2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007698,ECOCYC:G7202,GeneID:944847`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2448606-2449157:+; feature_type=gene
