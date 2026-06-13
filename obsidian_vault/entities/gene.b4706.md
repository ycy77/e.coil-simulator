---
entity_id: "gene.b4706"
entity_type: "gene"
name: "iroK"
source_database: "NCBI RefSeq"
source_id: "gene-b4706"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4706"
  - "iroK"
---

# iroK

`gene.b4706`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4706`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iroK (gene.b4706) is a gene entity. It encodes iroK (protein.U3PVA8). Encoded protein function: FUNCTION: Possible increased expression of this protein (due to mutations upstream of the start codon) is proposed to be responsible for resistance to 3-hydroxypropionic acid (3-HP). {ECO:0000269|PubMed:22161628}. EcoCyc product frame: MONOMER0-4224. Genomic coordinates: 2668006-2668071. EcoCyc protein note: Increased expression of IroK confers increased resistance to 3-hydroxypropionate .

## Biological Role

Repressed by C0293 (gene.b4806), hcaR (protein.Q47141).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.U3PVA8|protein.U3PVA8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4806|gene.b4806]] `RegulonDB` `S` - regulator=C0293; target=iroK; function=-
- `represses` <-- [[protein.Q47141|protein.Q47141]] `RegulonDB` `S` - regulator=HcaR; target=iroK; function=-

## External IDs

- `Dbxref:ECOCYC:G0-10716,GeneID:14678510`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2668006-2668071:-; feature_type=gene
