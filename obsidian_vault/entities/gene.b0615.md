---
entity_id: "gene.b0615"
entity_type: "gene"
name: "citF"
source_database: "NCBI RefSeq"
source_id: "gene-b0615"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0615"
  - "citF"
---

# citF

`gene.b0615`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0615`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citF (gene.b0615) is a gene entity. It encodes citF (protein.P75726). Encoded protein function: FUNCTION: Represents a citrate:acetyl-ACP transferase. {ECO:0000250}. EcoCyc product frame: CITTRANS-MONOMER. EcoCyc synonyms: ybdV. Genomic coordinates: 648039-649571.

## Biological Role

Activated by dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75726|protein.P75726]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=citF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002119,ECOCYC:G6341,GeneID:945230`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:648039-649571:-; feature_type=gene
