---
entity_id: "gene.b3440"
entity_type: "gene"
name: "yhhX"
source_database: "NCBI RefSeq"
source_id: "gene-b3440"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3440"
  - "yhhX"
---

# yhhX

`gene.b3440`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3440`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhhX (gene.b3440) is a gene entity. It encodes yhhX (protein.P46853). Encoded protein function: Uncharacterized oxidoreductase YhhX (EC 1.-.-.-) EcoCyc product frame: G7757-MONOMER. Genomic coordinates: 3579768-3580805. EcoCyc protein note: Based on sequence similarity, YhhX was predicted to be a D-galactose 1-dehydrogenase . However, this is not consistent with the known biochemistry of E. coli K-12, which metabolizes galactose via the PWY-6317. Transcription of yhhX was thought to be regulated by Fur , but the measured gene expression was due to a transcriptional fusion to ryhB . A transposon insertion mutant in yhhX is more sensitive to chloramphenicol than wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46853|protein.P46853]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011232,ECOCYC:G7757,GeneID:947944`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3579768-3580805:-; feature_type=gene
