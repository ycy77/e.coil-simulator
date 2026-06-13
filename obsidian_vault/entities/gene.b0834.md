---
entity_id: "gene.b0834"
entity_type: "gene"
name: "dgcI"
source_database: "NCBI RefSeq"
source_id: "gene-b0834"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0834"
  - "dgcI"
---

# dgcI

`gene.b0834`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0834`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcI (gene.b0834) is a gene entity. It encodes dgcI (protein.P75801). Encoded protein function: FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}. EcoCyc product frame: G6434-MONOMER. EcoCyc synonyms: yliF. Genomic coordinates: 875335-876663. EcoCyc protein note: DgcI belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . DgcI is an inner membrane protein with two predicted transmembrane domains; the C terminus is located in the cytoplasm . DgcI is predicted to be a bitopic inner membrane protein . DgcI contains an N-terminal GAPES (gamma-proteobacterial periplasmic sensory) domain . In a random transposon mutagenesis study, DgcI was found to be required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium . A dgcI mutant was found to be a weak suppressor of the synthetic lethal phenotype of a pta recBC(TS) strain . Expression of dgcI is downregulated by CsrA . DgcI: "diguanylate cyclase I" Review: .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75801|protein.P75801]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002841,ECOCYC:G6434,GeneID:945463`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:875335-876663:+; feature_type=gene
