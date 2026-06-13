---
entity_id: "gene.b3129"
entity_type: "gene"
name: "prlF"
source_database: "NCBI RefSeq"
source_id: "gene-b3129"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3129"
  - "prlF"
---

# prlF

`gene.b3129`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3129`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prlF (gene.b3129) is a gene entity. It encodes prlF (protein.P15373). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the YhaV toxin and neutralizes its ribonuclease activity. Also acts as a transcription factor. The YhaV/PrlF complex binds the prlF-yhaV operon, probably negatively regulating its expression. {ECO:0000269|PubMed:17706670}.; FUNCTION: Negatively regulates its own expression as well as relieving the export block imposed by high-level synthesis of the LamB-LacZ hybrid protein. Overexpression leads to increased doubling time and also suppresses a htrA (degP) null phenotype. {ECO:0000269|PubMed:17706670}. EcoCyc product frame: EG10955-MONOMER. EcoCyc synonyms: sohA, prlFA. Genomic coordinates: 3277002-3277337. EcoCyc protein note: PrlF is the antitoxin component in the PrlF-YhaV antitoxin-toxin complex. Overproduction of PrlF yields a growth defect and increased export of a reporter protein . prlF mutants show activated CPLX0-2881 activity, and suppression of heat sensitivity in htrA mutants . prlF htrA double mutants are cold sensitive . Review:

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15373|protein.P15373]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010287,ECOCYC:EG10955,GeneID:947639`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3277002-3277337:+; feature_type=gene
