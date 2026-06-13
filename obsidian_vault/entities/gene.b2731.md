---
entity_id: "gene.b2731"
entity_type: "gene"
name: "fhlA"
source_database: "NCBI RefSeq"
source_id: "gene-b2731"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2731"
  - "fhlA"
---

# fhlA

`gene.b2731`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2731`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhlA (gene.b2731) is a gene entity. It encodes fhlA (protein.P19323). Encoded protein function: FUNCTION: Required for induction of expression of the formate dehydrogenase H and hydrogenase-3 structural genes. Also activates expression of hyf operon (encodes the silent hydrogenase-4 gene cluster) (PubMed:12426353). {ECO:0000269|PubMed:12426353}. EcoCyc product frame: PD02936. EcoCyc synonyms: fhl. Genomic coordinates: 2854338-2856416.

## Biological Role

Activated by fnr (protein.P0A9E5), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19323|protein.P19323]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fhlA; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=fhlA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=fhlA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008971,ECOCYC:EG10301,GeneID:947181`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2854338-2856416:+; feature_type=gene
