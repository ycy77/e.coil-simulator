---
entity_id: "gene.b1420"
entity_type: "gene"
name: "mokB"
source_database: "NCBI RefSeq"
source_id: "gene-b1420"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1420"
  - "mokB"
---

# mokB

`gene.b1420`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1420`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mokB (gene.b1420) is a gene entity. It encodes mokB (protein.P76096). Encoded protein function: FUNCTION: Overlapping regulatory peptide whose translation enables hokB expression. {ECO:0000305}. EcoCyc product frame: G6736-MONOMER. Genomic coordinates: 1491962-1492129. EcoCyc protein note: The hokB/mokB/sokB locus of E. coli K-12 encodes an intact hok/sok toxin/antitoxin system . MokB: "mediation of killing B"

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76096|protein.P76096]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mokB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004738,ECOCYC:G6736,GeneID:948820`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1491962-1492129:-; feature_type=gene
