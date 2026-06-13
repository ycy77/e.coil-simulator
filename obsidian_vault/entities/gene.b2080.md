---
entity_id: "gene.b2080"
entity_type: "gene"
name: "yegP"
source_database: "NCBI RefSeq"
source_id: "gene-b2080"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2080"
  - "yegP"
---

# yegP

`gene.b2080`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2080`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegP (gene.b2080) is a gene entity. It encodes yegP (protein.P76402). Encoded protein function: UPF0339 protein YegP EcoCyc product frame: G7117-MONOMER. Genomic coordinates: 2165189-2165521. EcoCyc protein note: A ΔyegP mutant has a high number of aggravating genetic interactions in response to MMS with genes involved in the DNA damage response, DNA repair, replication and recombination. YegP may function in parallel with RecFOR in the double-strand break repair pathway .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76402|protein.P76402]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006888,ECOCYC:G7117,GeneID:947095`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2165189-2165521:+; feature_type=gene
