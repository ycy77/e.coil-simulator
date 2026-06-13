---
entity_id: "gene.b3901"
entity_type: "gene"
name: "rhaM"
source_database: "NCBI RefSeq"
source_id: "gene-b3901"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3901"
  - "rhaM"
---

# rhaM

`gene.b3901`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3901`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaM (gene.b3901) is a gene entity. It encodes rhaM (protein.P32156). Encoded protein function: FUNCTION: Involved in the anomeric conversion of L-rhamnose. {ECO:0000269|PubMed:15060078}. EcoCyc product frame: EG11865-MONOMER. EcoCyc synonyms: yiiL. Genomic coordinates: 4093124-4093438. EcoCyc protein note: Utilizing NMR techniques, RhaM was shown to catalyze the anomeric conversion of rhamnose . The enzyme has a preference for binding the β-anomer . A crystal structure of RhaM in complex with L-rhamnose was solved at 1.8 Å resolution. Analysis of the catalytic activity of mutants in predicted active site residues allowed the authors to propose a possible catalytic mechanism . A rhaM deletion mutant has a decreased growth rate when grown on low concentrations of L-rhamnose .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32156|protein.P32156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012729,ECOCYC:EG11865,GeneID:948402`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4093124-4093438:-; feature_type=gene
