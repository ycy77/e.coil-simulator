---
entity_id: "gene.b0189"
entity_type: "gene"
name: "rof"
source_database: "NCBI RefSeq"
source_id: "gene-b0189"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0189"
  - "rof"
---

# rof

`gene.b0189`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0189`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rof (gene.b0189) is a gene entity. It encodes rof (protein.P0AFW8). Encoded protein function: FUNCTION: Suppresses temperature-sensitive mutations in essential genes by modulating rho-dependent transcription termination. EcoCyc product frame: G6097-MONOMER. EcoCyc synonyms: yaeO. Genomic coordinates: 213678-213932. EcoCyc protein note: Rof interacts with the Rho terminator protein. It inhibits binding of Rho to ssDNA in vitro and shows antiterminator activity in vivo . The Rho transcription termination factor co-purifies with Rof. Expression of Rof reduces termination at the Rho-dependent terminator tL1 and rho itself in vivo . A solution structure of Rof has been determined. A docked model of the Rof-Rho complex based on NMR titrations suggests that Rof acts as a competitive inhibitor of Rho RNA binding. In vitro, Rof inhibits Rho binding to ssDNA . rof is a multicopy suppressor of temperature-sensitive alleles of genes such as ftsA, ftsQ, groEL, grpE, a malE-minE fusion allele , and an rpoB allele . Suppression appears to be due to antitermination . Expression of yaeP-rof is growth rate-regulated .

## Biological Role

Repressed by yidZ (protein.P31463).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFW8|protein.P0AFW8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P31463|protein.P31463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000641,ECOCYC:G6097,GeneID:944891`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:213678-213932:-; feature_type=gene
