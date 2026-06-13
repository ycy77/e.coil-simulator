---
entity_id: "gene.b0111"
entity_type: "gene"
name: "ampE"
source_database: "NCBI RefSeq"
source_id: "gene-b0111"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0111"
  - "ampE"
---

# ampE

`gene.b0111`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0111`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ampE (gene.b0111) is a gene entity. It encodes ampE (protein.P0AE14). Encoded protein function: FUNCTION: Putative signaling protein in beta-lactamase regulation. AmpE does not seem to act as a direct sensor for beta-lactams. EcoCyc product frame: EG10042-MONOMER. Genomic coordinates: 119281-120135. EcoCyc protein note: In contrast to some gram-negative species (Citrobacter freundii, Enterobacter cloacae, Pseudomonas aeruginosa and others), expression of the ampC encoded β-lactamase is non-inducible in E. coli K-12 due to the absence of ampR encoding a transcriptional regulator. Cloned ampC from C. freundii or E. cloacae is inducible in E. coli when accompanied by ampR (see and ). The closely linked genes, ampD and ampE, are implicated in the AmpR mediated regulation of AmpC in an E. coli K-12 strain containing cloned C. freundii ampR and ampC genes, but their role is not clear . AmpD was later characterized as an EG10041-MONOMER active during peptidoglycan recycling and its role in the induction of AmpC clarified (see reviews by ) but the function of AmpE remains unclear. ampE encodes an inner membrane protein; AmpE does not bind benzylpenicillin; ampE contains sequence motifs associated with ATP binding, it also contains 2 of the 3 motifs generally found in β-lactam reactive proteins...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE14|protein.P0AE14]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000382,ECOCYC:EG10042,GeneID:946678`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:119281-120135:+; feature_type=gene
