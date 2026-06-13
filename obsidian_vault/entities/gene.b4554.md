---
entity_id: "gene.b4554"
entity_type: "gene"
name: "yibT"
source_database: "NCBI RefSeq"
source_id: "gene-b4554"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4554"
  - "yibT"
---

# yibT

`gene.b4554`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4554`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yibT (gene.b4554) is a gene entity. It encodes yibT (protein.Q2M7R5). Encoded protein function: Uncharacterized protein YibT EcoCyc product frame: MONOMER0-2690. Genomic coordinates: 3776171-3776380. EcoCyc protein note: yibT was initially predicted as a short open reading frame (ORF) encoding a 69 residue protein and later detected in the proteome . yibT expression is downregulated in an E. coli K-12 strain engineered for increased tolerance to n-butanol . A ΔyibT strain has increased n-butanol tolerance and an increased proportion of unsaturated fatty acids (especially palmitoleic and oleic acid) in total fatty acids compared to wild type .

## Biological Role

Activated by lrp (protein.P0ACJ0), phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q2M7R5|protein.Q2M7R5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0285075,ECOCYC:G0-10468,GeneID:1450299`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3776171-3776380:-; feature_type=gene
