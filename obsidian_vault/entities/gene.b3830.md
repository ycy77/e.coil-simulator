---
entity_id: "gene.b3830"
entity_type: "gene"
name: "ysgA"
source_database: "NCBI RefSeq"
source_id: "gene-b3830"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3830"
  - "ysgA"
---

# ysgA

`gene.b3830`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3830`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ysgA (gene.b3830) is a gene entity. It encodes ysgA (protein.P56262). Encoded protein function: Putative carboxymethylenebutenolidase (EC 3.1.1.45) (Dienelactone hydrolase) (DLH) EcoCyc product frame: G7804-MONOMER. Genomic coordinates: 4015354-4016169. EcoCyc protein note: Using the COFACTOR pipeline, which combines analyses based on structure and sequence similarities and protein-protein interaction networks, YsgA was predicted to catalyze a reaction similar to EC-3.1.1.45 .

## Enriched Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00364` Fluorobenzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56262|protein.P56262]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012522,ECOCYC:G7804,GeneID:948320`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4015354-4016169:-; feature_type=gene
