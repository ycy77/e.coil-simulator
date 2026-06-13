---
entity_id: "gene.b2131"
entity_type: "gene"
name: "osmF"
source_database: "NCBI RefSeq"
source_id: "gene-b2131"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2131"
  - "osmF"
---

# osmF

`gene.b2131`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2131`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

osmF (gene.b2131) is a gene entity. It encodes yehZ (protein.P33362). Encoded protein function: FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Binds glycine betaine with low affinity. {ECO:0000269|PubMed:26325238}. EcoCyc product frame: YEHZ-MONOMER. EcoCyc synonyms: yehZ. Genomic coordinates: 2218564-2219481. EcoCyc protein note: OsmF is the periplasmic binding component of a low affinity glycine betaine ABC transporter; OsmF binds the osmoprotectants glycine betaine, choline-0-sulfate and dimethylsulfopropionate with low (mM) affinities . apoYehZ contains a type II periplasmic binding fold consisting of two domains (A and B) with two connecting loops . Expression of an osmF-phoA fusion is induced by growth in a medium of high osmolarity . An osmFlacZ transcriptional fusion is induced by both osmotic shock and entry into stationary phase .

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33362|protein.P33362]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=osmF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007040,ECOCYC:EG12012,GeneID:946681`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2218564-2219481:-; feature_type=gene
