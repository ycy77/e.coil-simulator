---
entity_id: "gene.b0098"
entity_type: "gene"
name: "secA"
source_database: "NCBI RefSeq"
source_id: "gene-b0098"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0098"
  - "secA"
---

# secA

`gene.b0098`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0098`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secA (gene.b0098) is a gene entity. It encodes secA (protein.P10408). Encoded protein function: FUNCTION: Required for protein export, interacts with the SecYEG preprotein conducting channel. SecA has a central role in coupling the hydrolysis of ATP to the transfer of proteins into and across the cell membrane, serving both as a receptor for the preprotein-SecB complex and as an ATP-driven molecular motor driving the stepwise translocation of polypeptide chains across the membrane. {ECO:0000269|PubMed:10931320, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:1825804, ECO:0000269|PubMed:1830665, ECO:0000269|PubMed:2846186}. EcoCyc product frame: SECA. EcoCyc synonyms: azi, pea, prlD. Genomic coordinates: 108279-110984.

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10408|protein.P10408]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000343,ECOCYC:EG10936,GeneID:944821`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:108279-110984:+; feature_type=gene
