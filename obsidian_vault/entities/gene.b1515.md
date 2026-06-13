---
entity_id: "gene.b1515"
entity_type: "gene"
name: "lsrD"
source_database: "NCBI RefSeq"
source_id: "gene-b1515"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1515"
  - "lsrD"
---

# lsrD

`gene.b1515`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1515`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lsrD (gene.b1515) is a gene entity. It encodes lsrD (protein.P0AFS1). Encoded protein function: FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305|PubMed:15601708}. EcoCyc product frame: YDEZ-MONOMER. EcoCyc synonyms: ydeZ. Genomic coordinates: 1604047-1605039. EcoCyc protein note: Based on sequence similarity lsrD is predicted to encode the membrane component of an AI-2 ABC transporter . lsrD is required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium .

## Biological Role

Repressed by lsrR (protein.P76141). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFS1|protein.P0AFS1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lsrD; function=+
- `represses` <-- [[protein.P76141|protein.P76141]] `RegulonDB` `C` - regulator=LsrR; target=lsrD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005061,ECOCYC:G6802,GeneID:946264`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1604047-1605039:+; feature_type=gene
