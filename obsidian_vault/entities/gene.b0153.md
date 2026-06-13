---
entity_id: "gene.b0153"
entity_type: "gene"
name: "fhuB"
source_database: "NCBI RefSeq"
source_id: "gene-b0153"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0153"
  - "fhuB"
---

# fhuB

`gene.b0153`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0153`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhuB (gene.b0153) is a gene entity. It encodes fhuB (protein.P06972). Encoded protein function: FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:1551849, ECO:0000269|PubMed:3020380, ECO:0000269|PubMed:34887516}. EcoCyc product frame: FHUB-MONOMER. Genomic coordinates: 171462-173444. EcoCyc protein note: FhuB is the integral membrane subunit of an iron(III) hydroxamate ABC transporter. FhuB consists of N and C terminal domains that have significant sequence similarity to each other; when expressed separately they can combine to form a functional permease; FhuB may function as a pseudo heterodimer

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06972|protein.P06972]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000526,ECOCYC:EG10303,GeneID:946890`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:171462-173444:+; feature_type=gene
