---
entity_id: "gene.b1968"
entity_type: "gene"
name: "hprS"
source_database: "NCBI RefSeq"
source_id: "gene-b1968"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1968"
  - "hprS"
---

# hprS

`gene.b1968`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1968`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hprS (gene.b1968) is a gene entity. It encodes hprS (protein.P76339). Encoded protein function: FUNCTION: Member of a two-component regulatory system HprR/HprS involved in response to hydrogen peroxide (PubMed:25568260, PubMed:27983483). Senses H(2)O(2), maybe via the redox state of the membrane (PubMed:27983483). Activates HprR by phosphorylation (PubMed:15522865). Can also phosphorylate CusR (PubMed:15522865). {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}. EcoCyc product frame: G7056-MONOMER. EcoCyc synonyms: yedV. Genomic coordinates: 2036794-2038152.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76339|protein.P76339]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006531,ECOCYC:G7056,GeneID:946487`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2036794-2038152:-; feature_type=gene
