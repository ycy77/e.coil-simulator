---
entity_id: "gene.b2223"
entity_type: "gene"
name: "atoE"
source_database: "NCBI RefSeq"
source_id: "gene-b2223"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2223"
  - "atoE"
---

# atoE

`gene.b2223`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2223`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atoE (gene.b2223) is a gene entity. It encodes atoE (protein.P76460). Encoded protein function: FUNCTION: May be responsible for the uptake of short-chain fatty acids. EcoCyc product frame: EG11671-MONOMER. Genomic coordinates: 2324756-2326078. EcoCyc protein note: AtoE is an inner membrane protein with ten predicted transmembrane domains. The C terminus is located in the periplasm .

## Biological Role

Activated by atoC (protein.Q06065).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76460|protein.P76460]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q06065|protein.Q06065]] `RegulonDB` `C` - regulator=AtoC; target=atoE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007353,ECOCYC:EG11671,GeneID:946721`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2324756-2326078:+; feature_type=gene
