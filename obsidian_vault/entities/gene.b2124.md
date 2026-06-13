---
entity_id: "gene.b2124"
entity_type: "gene"
name: "yehS"
source_database: "NCBI RefSeq"
source_id: "gene-b2124"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2124"
  - "yehS"
---

# yehS

`gene.b2124`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2124`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehS (gene.b2124) is a gene entity. It encodes yehS (protein.P33355). Encoded protein function: Uncharacterized protein YehS EcoCyc product frame: EG12005-MONOMER. Genomic coordinates: 2211726-2212196. EcoCyc protein note: Expression of yehS displayed lower variability across a number of E. coli populations adapted to different toxins . Repression of yehS expression leads to some growth improvement in the presence of n-butanol or n-hexane . A ΔyehS mutant shows an increased growth rate compared to wild type in the absence of biofuel stress .

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33355|protein.P33355]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yehS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007021,ECOCYC:EG12005,GeneID:949026`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2211726-2212196:-; feature_type=gene
