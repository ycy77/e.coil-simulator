---
entity_id: "gene.b3284"
entity_type: "gene"
name: "smg"
source_database: "NCBI RefSeq"
source_id: "gene-b3284"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3284"
  - "smg"
---

# smg

`gene.b3284`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3284`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

smg (gene.b3284) is a gene entity. It encodes smg (protein.P0A828). Encoded protein function: Protein Smg EcoCyc product frame: EG11605-MONOMER. Genomic coordinates: 3431991-3432464. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 20, 2017. smg: downstream of smf

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A828|protein.P0A828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=smg; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010770,ECOCYC:EG11605,GeneID:947781`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3431991-3432464:-; feature_type=gene
