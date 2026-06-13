---
entity_id: "gene.b1442"
entity_type: "gene"
name: "ydcU"
source_database: "NCBI RefSeq"
source_id: "gene-b1442"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1442"
  - "ydcU"
---

# ydcU

`gene.b1442`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1442`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcU (gene.b1442) is a gene entity. It encodes ydcU (protein.P77156). Encoded protein function: FUNCTION: Probably part of the ABC transporter complex YdcSTUV. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305}. EcoCyc product frame: YDCU-MONOMER. Genomic coordinates: 1513831-1514772. EcoCyc protein note: YdcU is the predicted inner membrane component of an uncharacterized ABC transporter .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77156|protein.P77156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ydcU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004807,ECOCYC:G6753,GeneID:945976`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1513831-1514772:+; feature_type=gene
