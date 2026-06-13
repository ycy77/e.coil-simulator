---
entity_id: "gene.b1516"
entity_type: "gene"
name: "lsrB"
source_database: "NCBI RefSeq"
source_id: "gene-b1516"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1516"
  - "lsrB"
---

# lsrB

`gene.b1516`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1516`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrB (gene.b1516) is a gene entity. It encodes lsrB (protein.P76142). Encoded protein function: FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Binds AI-2 and delivers it to the LsrC and LsrD permeases (Probable). {ECO:0000305|PubMed:15601708}. EcoCyc product frame: YNEA-MONOMER. EcoCyc synonyms: yneA. Genomic coordinates: 1605051-1606073. EcoCyc protein note: Based on sequence similarity lsrB is predicted to encode the periplasmic binding protein of an AI-2 ABC transporter . lsrB is overexpressed in E. coli biofilms compared to planktonic growth in exponential phase . LsrB binds the chemically synthesized probe D-desthiobiotin-AI-2 . A ΔlsrB::aphA strain is impaired in biofilm formation .

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76142|protein.P76142]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrB; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005063,ECOCYC:G6803,GeneID:945418`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1605051-1606073:+; feature_type=gene
