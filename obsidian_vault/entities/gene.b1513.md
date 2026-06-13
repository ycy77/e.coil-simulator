---
entity_id: "gene.b1513"
entity_type: "gene"
name: "lsrA"
source_database: "NCBI RefSeq"
source_id: "gene-b1513"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1513"
  - "lsrA"
---

# lsrA

`gene.b1513`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1513`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrA (gene.b1513) is a gene entity. It encodes lsrA (protein.P77257). Encoded protein function: FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Responsible for energy coupling to the transport system. {ECO:0000305|PubMed:15601708}. EcoCyc product frame: YDEX-MONOMER. EcoCyc synonyms: ego, ydeX. Genomic coordinates: 1601490-1603025. EcoCyc protein note: Based on sequence similarity lsrA is predicted to encode the ATP-binding component of an AI-2 ABC transporter . lsrA is required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium .

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77257|protein.P77257]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrA; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005056,ECOCYC:G6800,GeneID:945680`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1601490-1603025:+; feature_type=gene
