---
entity_id: "gene.b3783"
entity_type: "gene"
name: "rho"
source_database: "NCBI RefSeq"
source_id: "gene-b3783"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3783"
  - "rho"
---

# rho

`gene.b3783`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3783`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rho (gene.b3783) is a gene entity. It encodes rho (protein.P0AG30). Encoded protein function: FUNCTION: Facilitates transcription termination by a mechanism that involves Rho binding to the nascent RNA, activation of Rho's RNA-dependent ATPase activity, and release of the mRNA from the DNA template. RNA-dependent NTPase which utilizes all four ribonucleoside triphosphates as substrates. {ECO:0000269|PubMed:1716628, ECO:0000269|PubMed:2461932}. EcoCyc product frame: EG10845-MONOMER. EcoCyc synonyms: nusD, sun, tsu, rnsC, nitA, psu, psuA, sbaA. Genomic coordinates: 3966417-3967676.

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG30|protein.P0AG30]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=rho; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012362,ECOCYC:EG10845,GeneID:948297`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3966417-3967676:+; feature_type=gene
