---
entity_id: "gene.b3037"
entity_type: "gene"
name: "ygiB"
source_database: "NCBI RefSeq"
source_id: "gene-b3037"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3037"
  - "ygiB"
---

# ygiB

`gene.b3037`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3037`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiB (gene.b3037) is a gene entity. It encodes ygiB (protein.P0ADT2). Encoded protein function: UPF0441 protein YgiB EcoCyc product frame: EG11164-MONOMER. Genomic coordinates: 3179744-3180415. EcoCyc protein note: Transcription of ygiB is induced upon biofilm formation compared to planktonic growth in both exponential and stationary phase. Induction of expression was found to be dependent on the presence of the F plasmid . A ygiB mutant is impaired in biofilm formation . Deletion of ygiBC exacerbates the growth defects observed when E. coli tolC mutants are grown in glucose minimal media .

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADT2|protein.P0ADT2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ygiB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009969,ECOCYC:EG11164,GeneID:945086`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3179744-3180415:+; feature_type=gene
