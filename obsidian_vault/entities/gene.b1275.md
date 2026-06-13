---
entity_id: "gene.b1275"
entity_type: "gene"
name: "cysB"
source_database: "NCBI RefSeq"
source_id: "gene-b1275"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1275"
  - "cysB"
---

# cysB

`gene.b1275`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1275`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysB (gene.b1275) is a gene entity. It encodes cysB (protein.P0A9F3). Encoded protein function: FUNCTION: This protein is a positive regulator of gene expression for the cysteine regulon, a system of 10 or more loci involved in the biosynthesis of L-cysteine from inorganic sulfate. The inducer for CysB is N-acetylserine. CysB inhibits its own transcription. EcoCyc product frame: PD00232. Genomic coordinates: 1333855-1334829. EcoCyc protein note: The transcription factor CysB, for "Cysteine B," is negatively autoregulated ; this regulator also controls the transcription of the operon involved in novobiocin resistance and transcription of genes involved in sulfur utilization and sulfonate-sulfur catabolism via cysteine biosynthesis and in cysteine homeostasis . A role of CysB in hydrogen peroxide was suggested , because after 10 minutes of H2O2 at 2.5 mM exposure, various target genes of CysB were found upregulated, while in the cysB knockout mutant the upregulation of them was mitigated . Nonetheless, the cysB transcription level did not show an H2O2 dose-dependent regulation . Inhibition of cysB expression by CRISPRi enhanced cellular fitness under treatment with the antibiotics carbonyl cyanide 3-chlorophenylhydrazone (CCCP) or pyocyanin...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9F3|protein.P0A9F3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004279,ECOCYC:EG10184,GeneID:945771`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1333855-1334829:+; feature_type=gene
