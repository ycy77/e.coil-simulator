---
entity_id: "gene.b0800"
entity_type: "gene"
name: "ybiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0800"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0800"
  - "ybiB"
---

# ybiB

`gene.b0800`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0800`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiB (gene.b0800) is a gene entity. It encodes ybiB (protein.P30177). Encoded protein function: FUNCTION: DNA-binding protein that may be part of the LexA-controlled SOS response (PubMed:26063803). Binds with high affinity to DNA without sequence specificity (PubMed:26063803, PubMed:36864742). The difference in affinity between single- and double-stranded DNA is minor (PubMed:26063803). It also interacts with the GTPase ObgE, but does not influence ObgE GTP hydrolysis (PubMed:36864742). It may form a link between ObgE and the SOS response (PubMed:36864742). Does not show anthranilate phosphoribosyltransferase activity, nucleotide salvage activity or nucleoside phosphorylase activity (PubMed:26063803). {ECO:0000269|PubMed:26063803, ECO:0000269|PubMed:36864742}. EcoCyc product frame: EG11580-MONOMER. Genomic coordinates: 835248-836210.

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30177|protein.P30177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=ybiB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002734,ECOCYC:EG11580,GeneID:945424`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:835248-836210:+; feature_type=gene
