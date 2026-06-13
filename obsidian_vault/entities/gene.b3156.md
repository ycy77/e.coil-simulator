---
entity_id: "gene.b3156"
entity_type: "gene"
name: "yhbS"
source_database: "NCBI RefSeq"
source_id: "gene-b3156"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3156"
  - "yhbS"
---

# yhbS

`gene.b3156`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3156`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhbS (gene.b3156) is a gene entity. It encodes yhbS (protein.P63417). Encoded protein function: FUNCTION: Upon overexpression suppresses small RNA (sRNA)-mediated RhyB-silencing of multiple RNA targets; overexpression leads to partial loss of RhyB sRNA and other sRNAs. May act via Hfq. {ECO:0000269|PubMed:34210798}. EcoCyc product frame: G7650-MONOMER. Genomic coordinates: 3300255-3300758. EcoCyc protein note: When overexpressed, YhbS interferes with the function of the SRAI-RNA; it decreases the levels of several small RNAs . YhbS may act via its interaction with Hfq .

## Biological Role

Repressed by csgD (protein.P52106).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63417|protein.P63417]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=yhbS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010373,ECOCYC:G7650,GeneID:947670`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3300255-3300758:-; feature_type=gene
