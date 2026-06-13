---
entity_id: "gene.b2958"
entity_type: "gene"
name: "yggN"
source_database: "NCBI RefSeq"
source_id: "gene-b2958"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2958"
  - "yggN"
---

# yggN

`gene.b2958`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2958`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yggN (gene.b2958) is a gene entity. It encodes yggN (protein.P0ADS9). Encoded protein function: Uncharacterized protein YggN EcoCyc product frame: EG12705-MONOMER. EcoCyc synonyms: ecfF. Genomic coordinates: 3100904-3101623. EcoCyc protein note: Transcription of yggN is induced upon biofilm formation compared to planktonic growth in exponential phase. Induction of expression was found to be dependent on the presence of the F plasmid . A yggN mutant is impaired in biofilm formation .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADS9|protein.P0ADS9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yggN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009706,ECOCYC:EG12705,GeneID:947453`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3100904-3101623:-; feature_type=gene
