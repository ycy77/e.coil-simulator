---
entity_id: "gene.b2581"
entity_type: "gene"
name: "yfiF"
source_database: "NCBI RefSeq"
source_id: "gene-b2581"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2581"
  - "yfiF"
---

# yfiF

`gene.b2581`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2581`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiF (gene.b2581) is a gene entity. It encodes yfiF (protein.P0AGJ5). Encoded protein function: Uncharacterized tRNA/rRNA methyltransferase YfiF (EC 2.1.1.-) EcoCyc product frame: EG11786-MONOMER. Genomic coordinates: 2717491-2718528. EcoCyc protein note: YfiF appears to affect the initiation of DNA replication by influencing the content of DnaA per cell . YfiF physically interacts with G7950-MONOMER. Potential functional domains of YfiF were investigated by site-directed mutagenesis . A ΔyfiF mutant shows an increased doubling time and delayed initiation of replication; overexpression of yfiF leads to early initiation of replication .

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGJ5|protein.P0AGJ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=yfiF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008497,ECOCYC:EG11786,GeneID:947066`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2717491-2718528:-; feature_type=gene
