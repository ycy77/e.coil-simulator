---
entity_id: "gene.b2307"
entity_type: "gene"
name: "hisM"
source_database: "NCBI RefSeq"
source_id: "gene-b2307"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2307"
  - "hisM"
---

# hisM

`gene.b2307`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2307`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisM (gene.b2307) is a gene entity. It encodes hisM (protein.P0AEU3). Encoded protein function: FUNCTION: Part of the ABC transporter complex HisPMQJ involved in histidine transport. Is also part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000250|UniProtKB:P0A2I7}. EcoCyc product frame: HISM-MONOMER. Genomic coordinates: 2424517-2425233. EcoCyc protein note: HisM is one of two predicted integral membrane subunits of an ATP-dependent uptake system for the basic amino acids lysine, arginine, ornithine and histidine.

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEU3|protein.P0AEU3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=hisM; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=hisM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007613,ECOCYC:EG10007,GeneID:946790`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2424517-2425233:-; feature_type=gene
