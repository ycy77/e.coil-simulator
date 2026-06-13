---
entity_id: "gene.b0512"
entity_type: "gene"
name: "allB"
source_database: "NCBI RefSeq"
source_id: "gene-b0512"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0512"
  - "allB"
---

# allB

`gene.b0512`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0512`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allB (gene.b0512) is a gene entity. It encodes allB (protein.P77671). Encoded protein function: FUNCTION: Catalyzes the conversion of allantoin (5-ureidohydantoin) to allantoic acid by hydrolytic cleavage of the five-member hydantoin ring. {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:11092864}. EcoCyc product frame: G6281-MONOMER. EcoCyc synonyms: glxB3, ybbX. Genomic coordinates: 539147-540508.

## Biological Role

Repressed by allR (protein.P0ACN4).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77671|protein.P77671]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=allB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001768,ECOCYC:G6281,GeneID:945134`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:539147-540508:+; feature_type=gene
