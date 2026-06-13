---
entity_id: "gene.b0786"
entity_type: "gene"
name: "ybhL"
source_database: "NCBI RefSeq"
source_id: "gene-b0786"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0786"
  - "ybhL"
---

# ybhL

`gene.b0786`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0786`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybhL (gene.b0786) is a gene entity. It encodes ybhL (protein.P0AAC4). Encoded protein function: Inner membrane protein YbhL EcoCyc product frame: G6403-MONOMER. Genomic coordinates: 819884-820588. EcoCyc protein note: YbhL is an inner membrane protein ; it is predicted to contain seven transmembrane regions with the C- terminus located in the cytoplasm . In the Transporter Classification Database , YbhL is a member of the Calcium Transporter A (CaTA) family (formerly The Testis-Enhanced Gene Transfer (TEGT) Family, named after its prototypical member, Bax inhibitor 1 - formerly known as TEGT - testis enhanced gene transcript of Homo sapiens ).

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAC4|protein.P0AAC4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ybhL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002685,ECOCYC:G6403,GeneID:945401`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:819884-820588:+; feature_type=gene
