---
entity_id: "gene.b1514"
entity_type: "gene"
name: "lsrC"
source_database: "NCBI RefSeq"
source_id: "gene-b1514"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1514"
  - "lsrC"
---

# lsrC

`gene.b1514`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1514`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrC (gene.b1514) is a gene entity. It encodes lsrC (protein.P77672). Encoded protein function: FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305|PubMed:15601708}. EcoCyc product frame: YDEY-MONOMER. EcoCyc synonyms: ydeY. Genomic coordinates: 1603019-1604047. EcoCyc protein note: Based on sequence similarity lsrC is predicted to encode the membrane component of an AI-2 ABC transporter . lsrC is required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium .

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77672|protein.P77672]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrC; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005059,ECOCYC:G6801,GeneID:946105`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1603019-1604047:+; feature_type=gene
