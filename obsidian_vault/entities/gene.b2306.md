---
entity_id: "gene.b2306"
entity_type: "gene"
name: "hisP"
source_database: "NCBI RefSeq"
source_id: "gene-b2306"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2306"
  - "hisP"
---

# hisP

`gene.b2306`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2306`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisP (gene.b2306) is a gene entity. It encodes hisP (protein.P07109). Encoded protein function: FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Shows ATPase activity. Responsible for energy coupling to the transport system. {ECO:0000250|UniProtKB:P02915}. EcoCyc product frame: HISP-MONOMER. Genomic coordinates: 2423736-2424509. EcoCyc protein note: HisP is the predicted ATP binding subunit of an ATP-dependent uptake system for the basic amino acids lysine, arginine, ornithine and histidine. HisP contains signature motifs conserved in ATP-binding cassette (ABC) domains

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07109|protein.P07109]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=hisP; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=hisP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007610,ECOCYC:EG10452,GeneID:946789`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2423736-2424509:-; feature_type=gene
