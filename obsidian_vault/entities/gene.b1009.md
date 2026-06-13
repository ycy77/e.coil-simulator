---
entity_id: "gene.b1009"
entity_type: "gene"
name: "rutD"
source_database: "NCBI RefSeq"
source_id: "gene-b1009"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1009"
  - "rutD"
---

# rutD

`gene.b1009`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1009`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutD (gene.b1009) is a gene entity. It encodes rutD (protein.P75895). Encoded protein function: FUNCTION: Involved in pyrimidine catabolism (PubMed:16540542). May facilitate the hydrolysis of carbamate, a reaction that can also occur spontaneously (Probable). {ECO:0000269|PubMed:16540542, ECO:0000305|PubMed:33839153}. EcoCyc product frame: G6520-MONOMER. EcoCyc synonyms: ycdJ. Genomic coordinates: 1070965-1071765.

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75895|protein.P75895]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutD; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutD; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003410,ECOCYC:G6520,GeneID:946586`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1070965-1071765:-; feature_type=gene
