---
entity_id: "gene.b1433"
entity_type: "gene"
name: "ydcO"
source_database: "NCBI RefSeq"
source_id: "gene-b1433"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1433"
  - "ydcO"
---

# ydcO

`gene.b1433`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1433`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcO (gene.b1433) is a gene entity. It encodes ydcO (protein.P76103). Encoded protein function: Inner membrane protein YdcO EcoCyc product frame: B1433-MONOMER. Genomic coordinates: 1504905-1506080. EcoCyc protein note: YdcO is an uncharacterised member of the Benzoate:H+ Symporter (BenE) family within the Amino Acid-Polyamine-Organocation (APC) superfamily . Overexpression of ydcO* from a plasmid confers resistance to the toxic chemical, bromoacetate . *Please note: states: "We found that the ASKA ydcO clone contains 120 bp of genomic sequence preceding the ydcO coding sequence, which would be translated and fused to the N terminus of YdcO".

## Biological Role

Repressed by sutR (protein.P77626).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76103|protein.P76103]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=ydcO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004780,ECOCYC:G6744,GeneID:947247`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1504905-1506080:-; feature_type=gene
