---
entity_id: "gene.b3988"
entity_type: "gene"
name: "rpoC"
source_database: "NCBI RefSeq"
source_id: "gene-b3988"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3988"
  - "rpoC"
---

# rpoC

`gene.b3988`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3988`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoC (gene.b3988) is a gene entity. It encodes rpoC (protein.P0A8T7). Encoded protein function: FUNCTION: DNA-dependent RNA polymerase (RNAP) catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. {ECO:0000255|HAMAP-Rule:MF_01322, ECO:0000269|PubMed:1646077, ECO:0000269|PubMed:24843001}.; FUNCTION: Resistance to the antibiotics salinamide A, salinamide B, rifampicin, streptolydigin, CBR703, myxopyronin, and lipiarmycin can result from mutations in this protein. {ECO:0000269|PubMed:24843001, ECO:0000305|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}. EcoCyc product frame: RPOC-MONOMER. EcoCyc synonyms: tabB. Genomic coordinates: 4185350-4189573. EcoCyc protein note: Along with its β partner, the β' subunit of RNA polymerase is integrally involved in the enzymatic function of RNA polymerase, especially at the promoter melting stage. Both the β and β' subunits interact with DNA and may contribute to the polymerase active site...

## Enriched Pathways

- `eco03020` RNA polymerase (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8T7|protein.P0A8T7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013043,ECOCYC:EG10895,GeneID:948487`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4185350-4189573:+; feature_type=gene
