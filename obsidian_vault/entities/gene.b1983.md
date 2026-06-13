---
entity_id: "gene.b1983"
entity_type: "gene"
name: "yeeN"
source_database: "NCBI RefSeq"
source_id: "gene-b1983"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1983"
  - "yeeN"
---

# yeeN

`gene.b1983`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1983`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeeN (gene.b1983) is a gene entity. It encodes yeeN (protein.P0A8A2). Encoded protein function: Probable transcriptional regulatory protein YeeN EcoCyc product frame: G7068-MONOMER. Genomic coordinates: 2056858-2057574. EcoCyc protein note: In a study of the E. coli complexome, YeeN was found in a cytoplasmic complex together with YeeZ . A yeeN mutant has a cold-sensitive phenotype and is more sensitive to nalidixic acid and kasugamycin than wild type . YeeN was transcriptionally upregulated in iron limitation over iron excess at 63% dissolved oxygen as determined by RNA-seq .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8A2|protein.P0A8A2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006582,ECOCYC:G7068,GeneID:946493`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2056858-2057574:+; feature_type=gene
