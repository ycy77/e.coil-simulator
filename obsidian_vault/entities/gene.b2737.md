---
entity_id: "gene.b2737"
entity_type: "gene"
name: "ygbK"
source_database: "NCBI RefSeq"
source_id: "gene-b2737"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2737"
  - "ygbK"
---

# ygbK

`gene.b2737`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2737`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygbK (gene.b2737) is a gene entity. It encodes otnK (protein.Q46889). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of 3-oxo-tetronate to 3-oxo-tetronate 4-phosphate. {ECO:0000250|UniProtKB:P44093}. EcoCyc product frame: G7418-MONOMER. Genomic coordinates: 2862335-2863501. EcoCyc protein note: Although transcription of ygbK is regulated by σF (FliA) and FlhDC, neither mutation nor overexpression of ygbK result in defects in chemotaxis or flagellar motility .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46889|protein.Q46889]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008988,ECOCYC:G7418,GeneID:947199`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2862335-2863501:+; feature_type=gene
