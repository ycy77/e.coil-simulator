---
entity_id: "gene.b2714"
entity_type: "gene"
name: "ascG"
source_database: "NCBI RefSeq"
source_id: "gene-b2714"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2714"
  - "ascG"
---

# ascG

`gene.b2714`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2714`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ascG (gene.b2714) is a gene entity. It encodes ascG (protein.P24242). Encoded protein function: FUNCTION: Repressor of the asc operon. The cryptic operon is activated by the insertion of IS186 into the ascG gene. EcoCyc product frame: EG10087-MONOMER. EcoCyc synonyms: sac. Genomic coordinates: 2838254-2839264. EcoCyc protein note: The AscG, "Arbutin-salicin-cellibiose," transcriptional regulator represses the expression of a cryptic operon (ascFB) whose genes are involved in transport and utilization of the β-glucoside sugars arbutin, salicin, and cellibiose. This operon is activated only when the repressor is inactivated through the interruption of the gene by an insertion sequence . AscG also regulates prpBC for propionate catabolism . Consistent with a broader in vivo model for many transcription factors (including AscG), regulation is compatible with primary stabilization of RNAP at promoters, with fold-changes scaling approximately as the reciprocal of promoter basal activity and buffering promoter-to-promoter variability across contexts and perturbations . AscG is a GalR-type transcription factor and has a helix-turn-helix motif . AscG recognizes and binds the consensus palindromic sequence TGAAACCGGTTTCA . A high level of AscG is always present in wild-type Escherichia coli cells...

## Biological Role

Repressed by hns (protein.P0ACF8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24242|protein.P24242]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008922,ECOCYC:EG10087,GeneID:947305`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2838254-2839264:-; feature_type=gene
