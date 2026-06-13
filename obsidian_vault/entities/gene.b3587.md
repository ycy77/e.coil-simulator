---
entity_id: "gene.b3587"
entity_type: "gene"
name: "yiaW"
source_database: "NCBI RefSeq"
source_id: "gene-b3587"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3587"
  - "yiaW"
---

# yiaW

`gene.b3587`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3587`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaW (gene.b3587) is a gene entity. It encodes yiaW (protein.P0ADK4). Encoded protein function: Inner membrane protein YiaW EcoCyc product frame: EG12291-MONOMER. Genomic coordinates: 3754105-3754428. EcoCyc protein note: YiaW is predicted to be an inner membrane protein with two transmembrane domains; experimental topology analysis suggest the C-terminus is located in the cytoplasm . A transposon insertion in the intergenic region between yiaW and aldB causes increased sensitivity to various antimicrobial drugs, but a yiaW deletion mutant shows no such effect .

## Biological Role

Activated by yiaU (protein.P37682).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADK4|protein.P0ADK4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37682|protein.P37682]] `RegulonDB` `C` - regulator=YiaU; target=yiaW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011714,ECOCYC:EG12291,GeneID:948105`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3754105-3754428:-; feature_type=gene
