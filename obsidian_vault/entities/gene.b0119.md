---
entity_id: "gene.b0119"
entity_type: "gene"
name: "yacL"
source_database: "NCBI RefSeq"
source_id: "gene-b0119"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0119"
  - "yacL"
---

# yacL

`gene.b0119`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0119`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yacL (gene.b0119) is a gene entity. It encodes yacL (protein.P0A8E5). Encoded protein function: UPF0231 protein YacL EcoCyc product frame: EG12605-MONOMER. Genomic coordinates: 134388-134750. EcoCyc protein note: YacL was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . Crosslinking mass spectrometry-based protein-protein interaction data has placed the YacL protein near the DNA exit tunnel of RNA polymerase . A yacL in-frame deletion strain has been constructed . Expression of YacL is negatively regulated by the small RNA CyaR .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8E5|protein.P0A8E5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000414,ECOCYC:EG12605,GeneID:944809`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:134388-134750:+; feature_type=gene
