---
entity_id: "gene.b4461"
entity_type: "gene"
name: "yfjD"
source_database: "NCBI RefSeq"
source_id: "gene-b4461"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4461"
  - "yfjD"
---

# yfjD

`gene.b4461`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4461`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfjD (gene.b4461) is a gene entity. It encodes yfjD (protein.P37908). Encoded protein function: UPF0053 inner membrane protein YfjD EcoCyc product frame: G7356-MONOMER. EcoCyc synonyms: b2612, ypjE, b2613. Genomic coordinates: 2748774-2750060. EcoCyc protein note: YfjD is predicted to be an inner membrane protein with four transmembrane domains; experiemntal topology analysis suggests the C terminus is located in the cytoplasm . A yfjD deletion mutant is more sensitive to nalidixic acid and kasugamycin than wild type .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37908|protein.P37908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yfjD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174111,ECOCYC:EG12442,GeneID:2847739`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2748774-2750060:+; feature_type=gene
