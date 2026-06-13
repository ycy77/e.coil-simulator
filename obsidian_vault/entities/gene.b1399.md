---
entity_id: "gene.b1399"
entity_type: "gene"
name: "paaX"
source_database: "NCBI RefSeq"
source_id: "gene-b1399"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1399"
  - "paaX"
---

# paaX

`gene.b1399`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1399`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaX (gene.b1399) is a gene entity. It encodes paaX (protein.P76086). Encoded protein function: FUNCTION: Negative regulator of the paaZ and paaABCDEFGHIJK catabolic operons. Binds the consensus sequence 5'-WWTRTGATTCGYGWT-3'. Binding of PaaX is specifically inhibited by phenylacetyl-coenzyme A (PA-CoA). {ECO:0000269|PubMed:10766858, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6720-MONOMER. EcoCyc synonyms: ydbY. Genomic coordinates: 1463539-1464489.

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76086|protein.P76086]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaX; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `S` - regulator=PaaX; target=paaX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004674,ECOCYC:G6720,GeneID:945966`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1463539-1464489:+; feature_type=gene
