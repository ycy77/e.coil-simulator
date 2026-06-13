---
entity_id: "gene.b1895"
entity_type: "gene"
name: "uspC"
source_database: "NCBI RefSeq"
source_id: "gene-b1895"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1895"
  - "uspC"
---

# uspC

`gene.b1895`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1895`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspC (gene.b1895) is a gene entity. It encodes uspC (protein.P46888). Encoded protein function: FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}. EcoCyc product frame: G7031-MONOMER. EcoCyc synonyms: yecG. Genomic coordinates: 1979753-1980181.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46888|protein.P46888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=uspC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006316,ECOCYC:G7031,GeneID:946404`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1979753-1980181:+; feature_type=gene
