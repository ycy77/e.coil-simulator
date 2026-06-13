---
entity_id: "gene.b1745"
entity_type: "gene"
name: "astB"
source_database: "NCBI RefSeq"
source_id: "gene-b1745"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1745"
  - "astB"
---

# astB

`gene.b1745`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1745`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

astB (gene.b1745) is a gene entity. It encodes astB (protein.P76216). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of N(2)-succinylarginine into N(2)-succinylornithine, ammonia and CO(2). {ECO:0000269|PubMed:15703173, ECO:0000269|PubMed:9696779}. EcoCyc product frame: SUCCARGDIHYDRO-MONOMER. EcoCyc synonyms: ydjT. Genomic coordinates: 1826916-1828259.

## Biological Role

Activated by argR (protein.P0A6D0), glnG (protein.P0AFB8), rpoS (protein.P13445), rpoN (protein.P24255).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76216|protein.P76216]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=astB; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=astB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=astB; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `C` - sigma=sigma54; target=astB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005817,ECOCYC:G6941,GeneID:946259`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1826916-1828259:-; feature_type=gene
