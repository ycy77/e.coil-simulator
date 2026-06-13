---
entity_id: "gene.b4256"
entity_type: "gene"
name: "yjgM"
source_database: "NCBI RefSeq"
source_id: "gene-b4256"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4256"
  - "yjgM"
---

# yjgM

`gene.b4256`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4256`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjgM (gene.b4256) is a gene entity. It encodes yjgM (protein.P39337). Encoded protein function: Uncharacterized N-acetyltransferase YjgM (EC 2.3.1.-) EcoCyc product frame: G7886-MONOMER. Genomic coordinates: 4479034-4479537. EcoCyc protein note: The ortholog from Salmonella enterica, OatA, catalyzes the acetylation of the Nα-amino group of O-acetylserine to produce N,O-diacetylserine .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39337|protein.P39337]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjgM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013939,ECOCYC:G7886,GeneID:948772`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4479034-4479537:-; feature_type=gene
