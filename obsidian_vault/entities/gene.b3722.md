---
entity_id: "gene.b3722"
entity_type: "gene"
name: "bglF"
source_database: "NCBI RefSeq"
source_id: "gene-b3722"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3722"
  - "bglF"
---

# bglF

`gene.b3722`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3722`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglF (gene.b3722) is a gene entity. It encodes bglF (protein.P08722). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in beta-glucoside transport.; FUNCTION: Acts both as a kinase and as a phosphatase on BglG. EcoCyc product frame: BGLF-MONOMER. EcoCyc synonyms: bglS. Genomic coordinates: 3903720-3905597.

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8). Activated by crp (protein.P0ACJ8), leuO (protein.P10151).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08722|protein.P08722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=bglF; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=bglF; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=bglF; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=bglF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012171,ECOCYC:EG10115,GeneID:948236`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3903720-3905597:-; feature_type=gene
