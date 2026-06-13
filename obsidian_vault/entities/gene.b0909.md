---
entity_id: "gene.b0909"
entity_type: "gene"
name: "ycaL"
source_database: "NCBI RefSeq"
source_id: "gene-b0909"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0909"
  - "ycaL"
---

# ycaL

`gene.b0909`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0909`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaL (gene.b0909) is a gene entity. It encodes ycaL (protein.P43674). Encoded protein function: FUNCTION: Involved in the degradation of the LPS-assembly protein LptD. Degrades LptD that have engaged the Bam complex but are stalled at an early step in the outer membrane protein assembly process. {ECO:0000269|PubMed:28784813}. EcoCyc product frame: G6470-MONOMER. Genomic coordinates: 960264-961028. EcoCyc protein note: YcaL belongs to the widely conserved M48 family of metalloproteases . YcaL is a predicted lipoprotein . YcaL degrades mutant EG11569-MONOMER LptD (LptDY721D) that is stalled for processing on the Bam complex but is still competent for Bam-mediated LptDE translocon assembly; the periplasmic proteases YcaL, G7311-MONOMER BepA and CPLX0-2921 DegP degrade stalled LptD substrate at different stages in the OMP assembly process .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43674|protein.P43674]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003098,ECOCYC:G6470,GeneID:945534`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:960264-961028:+; feature_type=gene
