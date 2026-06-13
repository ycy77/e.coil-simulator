---
entity_id: "gene.b4145"
entity_type: "gene"
name: "yjeJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4145"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4145"
  - "yjeJ"
---

# yjeJ

`gene.b4145`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4145`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjeJ (gene.b4145) is a gene entity. It encodes yjeJ (protein.P39279). Encoded protein function: Uncharacterized protein YjeJ EcoCyc product frame: G7835-MONOMER. Genomic coordinates: 4373365-4374234. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 13, 2013.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39279|protein.P39279]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjeJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013575,ECOCYC:G7835,GeneID:948663`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4373365-4374234:-; feature_type=gene
