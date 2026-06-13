---
entity_id: "gene.b2456"
entity_type: "gene"
name: "eutN"
source_database: "NCBI RefSeq"
source_id: "gene-b2456"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2456"
  - "eutN"
---

# eutN

`gene.b2456`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2456`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutN (gene.b2456) is a gene entity. It encodes eutN (protein.P0AEJ8). Encoded protein function: FUNCTION: Probably forms vertices in the bacterial microcompartment (BMC) dedicated to ethanolamine degradation (Probable). It may be involved in transporting positively charged molecules into and out of the BMC (Probable). {ECO:0000305|PubMed:17588214, ECO:0000305|PubMed:23456886}. EcoCyc product frame: G7286-MONOMER. EcoCyc synonyms: yffY, cchB. Genomic coordinates: 2571763-2572050. EcoCyc protein note: Several genes of the eut operon are involved in the ability to utilize ethanolamine as the sole source of carbon and nitrogen in Salmonella typhimurium; the operon is conserved between Salmonella and E. coli. EutN has not been shown to be involved in ethanolamine utilization in either Salmonella or E. coli . EutN is similar to the carboxysomal shell protein CcmL of Synechococcus sp. strain PCC7942 . A crystal structure of EutN has been solved at 2.4 Å resolution. The protein forms a tight hexamer with a central hole that is predominantly covered by acidic residues, suggesting a pore with a transport function . EutN: "ethanolamine utilization" CchB: "carbon dioxide concentration homolog B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEJ8|protein.P0AEJ8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008093,ECOCYC:G7286,GeneID:946945`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2571763-2572050:-; feature_type=gene
