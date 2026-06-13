---
entity_id: "gene.b3818"
entity_type: "gene"
name: "yigG"
source_database: "NCBI RefSeq"
source_id: "gene-b3818"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3818"
  - "yigG"
---

# yigG

`gene.b3818`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3818`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yigG (gene.b3818) is a gene entity. It encodes yigG (protein.P27843). Encoded protein function: Inner membrane protein YigG EcoCyc product frame: EG11465-MONOMER. Genomic coordinates: 4002813-4003193. EcoCyc protein note: Protein topology in the inner membrane has been determined .

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27843|protein.P27843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yigG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012468,ECOCYC:EG11465,GeneID:948344`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4002813-4003193:-; feature_type=gene
