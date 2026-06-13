---
entity_id: "gene.b3569"
entity_type: "gene"
name: "xylR"
source_database: "NCBI RefSeq"
source_id: "gene-b3569"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3569"
  - "xylR"
---

# xylR

`gene.b3569`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3569`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylR (gene.b3569) is a gene entity. It encodes xylR (protein.P0ACI3). Encoded protein function: FUNCTION: Regulatory protein for the xylBAFGHR operon. EcoCyc product frame: EG20253-MONOMER. Genomic coordinates: 3734979-3736157.

## Biological Role

Repressed by dicF (gene.b1574). Activated by xylR (protein.P0ACI3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACI3|protein.P0ACI3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylR; function=+
- `represses` <-- [[gene.b1574|gene.b1574]] `RegulonDB` `S` - regulator=DicF; target=xylR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011652,ECOCYC:EG20253,GeneID:948086`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3734979-3736157:+; feature_type=gene
