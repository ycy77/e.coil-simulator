---
entity_id: "gene.b0719"
entity_type: "gene"
name: "ybgD"
source_database: "NCBI RefSeq"
source_id: "gene-b0719"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0719"
  - "ybgD"
---

# ybgD

`gene.b0719`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0719`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybgD (gene.b0719) is a gene entity. It encodes ybgD (protein.P37909). Encoded protein function: Uncharacterized fimbrial-like protein YbgD EcoCyc product frame: EG12359-MONOMER. Genomic coordinates: 752229-752795. EcoCyc protein note: Sequence similarity suggests that YbgD is a fimbrial protein, potentially the major subunit . The operon is considered cryptic under normal laboratory conditions tested. However, YbgD was extracted from the surface protein mileau of an E. coli strain consitutively expressing the putative chaperone-usher fimbrial operon, ybgOPQD. In a ΔEG10457 background, expression of the ybgOPQD operon was increased and displayed arabinose-dependent complementation; CPLX0-226 CRP-cAMP is a positive regulator as observed in a double ΔhnsΔcrp mutant . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ybgOPQD. When this operon is removed, the cells are larger, produce polyhydroxyalkanoates (PHAs) and grows better. A fimbrial-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised; it also grows faster and produces PHAs and had higher efficiency of glucose utilization .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37909|protein.P37909]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002448,ECOCYC:EG12359,GeneID:945325`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:752229-752795:-; feature_type=gene
