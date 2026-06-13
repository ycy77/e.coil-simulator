---
entity_id: "gene.b2930"
entity_type: "gene"
name: "yggF"
source_database: "NCBI RefSeq"
source_id: "gene-b2930"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2930"
  - "yggF"
---

# yggF

`gene.b2930`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2930`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yggF (gene.b2930) is a gene entity. It encodes yggF (protein.P21437). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of fructose 1,6-bisphosphate to fructose 6-phosphate. Also displays a low activity toward glucose 1,6-bisphosphate, and no activity against ribulose 1,5-bisphosphate, fructose 2,6-bisphosphate, or fructose 1-phosphate. {ECO:0000269|PubMed:19073594}. EcoCyc product frame: EG11245-MONOMER. EcoCyc synonyms: yggK. Genomic coordinates: 3075217-3076182.

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21437|protein.P21437]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009615,ECOCYC:EG11245,GeneID:947410`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3075217-3076182:-; feature_type=gene
