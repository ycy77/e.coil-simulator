---
entity_id: "gene.b3497"
entity_type: "gene"
name: "rsmJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3497"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3497"
  - "rsmJ"
---

# rsmJ

`gene.b3497`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3497`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmJ (gene.b3497) is a gene entity. It encodes rsmJ (protein.P68567). Encoded protein function: FUNCTION: Specifically methylates the guanosine in position 1516 of 16S rRNA. {ECO:0000255|HAMAP-Rule:MF_01523, ECO:0000269|PubMed:22079366}. EcoCyc product frame: EG12233-MONOMER. EcoCyc synonyms: yhiQ. Genomic coordinates: 3642380-3643132. EcoCyc protein note: RsmJ is the methyltransferase responsible for methylation of 16S rRNA at the N2 position of the G1516 nucleotide. In vitro, the enzyme can methylate 16S rRNA within the 30S ribosomal subunit, but not free 16S rRNA . prlC-rsmJ is a heat shock operon regulated by RpoH . An rsmJ mutant strain is cold sensitive, showing a growth defect at 16°C .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68567|protein.P68567]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011419,ECOCYC:EG12233,GeneID:948005`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3642380-3643132:-; feature_type=gene
