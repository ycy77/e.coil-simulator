---
entity_id: "gene.b1700"
entity_type: "gene"
name: "ydiT"
source_database: "NCBI RefSeq"
source_id: "gene-b1700"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1700"
  - "ydiT"
---

# ydiT

`gene.b1700`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1700`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiT (gene.b1700) is a gene entity. It encodes ydiT (protein.P77714). Encoded protein function: FUNCTION: Could be a 3Fe-4S cluster-containing protein. Probably participates in a redox process with YdiQ, YdiR and YdiS. EcoCyc product frame: G6923-MONOMER. Genomic coordinates: 1782681-1782974. EcoCyc protein note: YdiT is predicted to be a ferredoxin. YdiO, YdiQ, YdiR, YdiS, and YdiT may play a role in electron transport between the anaerobic fatty acid oxidation pathway and the respiratory chain .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77714|protein.P77714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005674,ECOCYC:G6923,GeneID:946214`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1782681-1782974:+; feature_type=gene
