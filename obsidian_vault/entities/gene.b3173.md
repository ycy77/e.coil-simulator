---
entity_id: "gene.b3173"
entity_type: "gene"
name: "yhbX"
source_database: "NCBI RefSeq"
source_id: "gene-b3173"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3173"
  - "yhbX"
---

# yhbX

`gene.b3173`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3173`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhbX (gene.b3173) is a gene entity. It encodes yhbX (protein.P42640). Encoded protein function: FUNCTION: Probably does not transfer phosphoethanolamine to lipid A. {ECO:0000250|UniProtKB:P58216}. EcoCyc product frame: G7655-MONOMER. Genomic coordinates: 3319988-3321613. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 13, 2018.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42640|protein.P42640]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhbX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010430,ECOCYC:G7655,GeneID:947711`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3319988-3321613:-; feature_type=gene
