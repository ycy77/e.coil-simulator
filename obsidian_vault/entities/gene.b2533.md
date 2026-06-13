---
entity_id: "gene.b2533"
entity_type: "gene"
name: "suhB"
source_database: "NCBI RefSeq"
source_id: "gene-b2533"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2533"
  - "suhB"
---

# suhB

`gene.b2533`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2533`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

suhB (gene.b2533) is a gene entity. It encodes suhB (protein.P0ADG4). Encoded protein function: FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. This subunit may play a central role in organizing the structure (PubMed:32871103). Involved in 30S ribosomal subunit biogenesis; thought to be required for loop formation between NusB/NusE (rpsJ, ribosomal protein S10) bound to boxA upstream of the rRNA operons and the elongating RNAP complex. This would promote correct co-transcriptional folding of rRNA. Plays a role in transcription antitermination in a plasmid context in vivo (PubMed:26980831). Required for rrn transcription antitermination; required for integration of NusB/NusE into the antitermination complex (PubMed:31020314). The Nus factor complex (NusA, NusB, NusE (rpsJ), NusG and SuhB) represses expression of suhB and possibly other genes via boxA; the Nus complex prevents or promotes Rho-mediated transcription termination depending on gene context (PubMed:29229908). Involved in post-transcriptional control of gene expression (Probable)...

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADG4|protein.P0ADG4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:EG10983,GeneID:947285`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2663442-2664245:+; feature_type=gene
