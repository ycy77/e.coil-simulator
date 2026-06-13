---
entity_id: "gene.b2308"
entity_type: "gene"
name: "hisQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2308"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2308"
  - "hisQ"
---

# hisQ

`gene.b2308`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2308`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisQ (gene.b2308) is a gene entity. It encodes hisQ (protein.P52094). Encoded protein function: FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000250|UniProtKB:P0A2I9}. EcoCyc product frame: HISQ-MONOMER. Genomic coordinates: 2425230-2425916. EcoCyc protein note: HisQ is one of two predicted integral membrane subunits of an ATP-dependent uptake system for the basic amino acids lysine, arginine, ornithine and histidine.

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52094|protein.P52094]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=hisQ; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=hisQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007615,ECOCYC:EG12125,GeneID:947235`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2425230-2425916:-; feature_type=gene
