---
entity_id: "gene.b3351"
entity_type: "gene"
name: "kefG"
source_database: "NCBI RefSeq"
source_id: "gene-b3351"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3351"
  - "kefG"
---

# kefG

`gene.b3351`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3351`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kefG (gene.b3351) is a gene entity. It encodes kefG (protein.P0A756). Encoded protein function: FUNCTION: Regulatory subunit of a potassium efflux system that confers protection against electrophiles. Required for full activity of KefB. {ECO:0000255|HAMAP-Rule:MF_01415, ECO:0000269|PubMed:11053405}. EcoCyc product frame: G7717-MONOMER. EcoCyc synonyms: yheR. Genomic coordinates: 3480607-3481161. EcoCyc protein note: KefG is required for KefB activity . Based on sequence similarity, KefG was predicted to be an NAD(P)H dehydrogenase . However, the protein appears to lack conserved essential residues .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A756|protein.P0A756]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010951,ECOCYC:G7717,GeneID:947857`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3480607-3481161:-; feature_type=gene
