---
entity_id: "gene.b2700"
entity_type: "gene"
name: "pncC"
source_database: "NCBI RefSeq"
source_id: "gene-b2700"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2700"
  - "pncC"
---

# pncC

`gene.b2700`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2700`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pncC (gene.b2700) is a gene entity. It encodes pncC (protein.P0A6G3). Encoded protein function: FUNCTION: Has nicotinamidemononucleotide (NMN) aminohydrolase activity, not active on other substrates. {ECO:0000269|PubMed:21953451}. EcoCyc product frame: G7409-MONOMER. EcoCyc synonyms: ygaD. Genomic coordinates: 2823849-2824346.

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6G3|protein.P0A6G3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=pncC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008882,ECOCYC:G7409,GeneID:947169`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2823849-2824346:-; feature_type=gene
