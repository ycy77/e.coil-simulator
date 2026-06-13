---
entity_id: "gene.b3939"
entity_type: "gene"
name: "metB"
source_database: "NCBI RefSeq"
source_id: "gene-b3939"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3939"
  - "metB"
---

# metB

`gene.b3939`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3939`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metB (gene.b3939) is a gene entity. It encodes metB (protein.P00935). Encoded protein function: FUNCTION: Catalyzes the formation of L-cystathionine from O-succinyl-L-homoserine (OSHS) and L-cysteine, via a gamma-replacement reaction. In the absence of thiol, catalyzes gamma-elimination to form 2-oxobutanoate, succinate and ammonia. {ECO:0000269|PubMed:2405903}. EcoCyc product frame: O-SUCCHOMOSERLYASE-MONOMER. EcoCyc synonyms: met-1. Genomic coordinates: 4128672-4129832.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00935|protein.P00935]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012887,ECOCYC:EG10582,GeneID:948434`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4128672-4129832:+; feature_type=gene
