---
entity_id: "gene.b0855"
entity_type: "gene"
name: "potG"
source_database: "NCBI RefSeq"
source_id: "gene-b0855"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0855"
  - "potG"
---

# potG

`gene.b0855`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0855`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potG (gene.b0855) is a gene entity. It encodes potG (protein.P31134). Encoded protein function: FUNCTION: Part of the ABC transporter complex PotFGHI involved in putrescine uptake (PubMed:23719730, PubMed:8416922). Responsible for energy coupling to the transport system (PubMed:23719730). Imports putrescine for maintenance of the optimal concentration of polyamines necessary for cell growth in the presence of glucose (PubMed:23719730). {ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:8416922}. EcoCyc product frame: POTG-MONOMER. Genomic coordinates: 894991-896124. EcoCyc protein note: potG encodes the predicted ATP-binding subunit of a putrescine uptake system; PotG contains signature motifs coserved in ATP-binding cassette (ABC) proteins . PotG has 42% sequence similarity with PotA - the ATP-binding subunit of the spermidine ABC transporter .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31134|protein.P31134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002915,ECOCYC:EG11630,GeneID:945476`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:894991-896124:+; feature_type=gene
