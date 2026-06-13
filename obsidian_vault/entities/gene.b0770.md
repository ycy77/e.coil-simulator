---
entity_id: "gene.b0770"
entity_type: "gene"
name: "ybhI"
source_database: "NCBI RefSeq"
source_id: "gene-b0770"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0770"
  - "ybhI"
---

# ybhI

`gene.b0770`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0770`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhI (gene.b0770) is a gene entity. It encodes ybhI (protein.P75763). Encoded protein function: Inner membrane protein YbhI EcoCyc product frame: B0770-MONOMER. Genomic coordinates: 801887-803320. EcoCyc protein note: YbhI has 35% sequence identity with the citrate:succinate antiporter, CitT; ybhI is predicted to encode a tricarboxylic acid transporter . In the Transporter Classification Database, YbhI is a member of the Divalent Anion:Na+ Symporter (DASS) family . Experimental activation of ybhI expression (by a Tn5 transposase-based system) improves glycine tolerance .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75763|protein.P75763]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybhI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002621,ECOCYC:G6400,GeneID:945377`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:801887-803320:+; feature_type=gene
