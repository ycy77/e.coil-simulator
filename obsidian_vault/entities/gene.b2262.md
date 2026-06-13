---
entity_id: "gene.b2262"
entity_type: "gene"
name: "menB"
source_database: "NCBI RefSeq"
source_id: "gene-b2262"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2262"
  - "menB"
---

# menB

`gene.b2262`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2262`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menB (gene.b2262) is a gene entity. It encodes menB (protein.P0ABU0). Encoded protein function: FUNCTION: Converts o-succinylbenzoyl-CoA (OSB-CoA) to 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA). {ECO:0000255|HAMAP-Rule:MF_01934, ECO:0000269|PubMed:1091286, ECO:0000269|PubMed:20643650, ECO:0000269|PubMed:21830810, ECO:0000269|PubMed:23658663}. EcoCyc product frame: NAPHTHOATE-SYN-MONOMER. Genomic coordinates: 2375962-2376819.

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABU0|protein.P0ABU0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007476,ECOCYC:EG11368,GeneID:946747`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2375962-2376819:-; feature_type=gene
