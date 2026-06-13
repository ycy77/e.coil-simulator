---
entity_id: "gene.b3478"
entity_type: "gene"
name: "nikC"
source_database: "NCBI RefSeq"
source_id: "gene-b3478"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3478"
  - "nikC"
---

# nikC

`gene.b3478`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3478`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nikC (gene.b3478) is a gene entity. It encodes nikC (protein.P0AFA9). Encoded protein function: FUNCTION: Involved in a nickel transport system, probably translocates nickel through the bacterial inner membrane. EcoCyc product frame: NIKC-MONOMER. EcoCyc synonyms: hydD, hydC. Genomic coordinates: 3616182-3617015. EcoCyc protein note: NikC is one of two predicted inner membrane subunits of a high affinity uptake system for Ni2+; NikC contains six potential transmembrane α-helices .

## Biological Role

Repressed by nikR (protein.P0A6Z6). Activated by fnr (protein.P0A9E5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFA9|protein.P0AFA9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nikC; function=+
- `represses` <-- [[protein.P0A6Z6|protein.P0A6Z6]] `RegulonDB` `S` - regulator=NikR; target=nikC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011358,ECOCYC:EG12077,GeneID:947990`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3616182-3617015:+; feature_type=gene
