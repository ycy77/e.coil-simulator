---
entity_id: "gene.b3925"
entity_type: "gene"
name: "glpX"
source_database: "NCBI RefSeq"
source_id: "gene-b3925"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3925"
  - "glpX"
---

# glpX

`gene.b3925`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3925`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpX (gene.b3925) is a gene entity. It encodes glpX (protein.P0A9C9). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of fructose 1,6-bisphosphate to fructose 6-phosphate. Is likely to be involved in gluconeogenesis during growth on glycerol. Also displays a low activity toward glucose 1,6-bisphosphate, and no activity against ribulose 1,5-bisphosphate, fructose 2,6-bisphosphate, or fructose 1-phosphate. {ECO:0000269|PubMed:10986273, ECO:0000269|PubMed:19073594}. EcoCyc product frame: EG11517-MONOMER. Genomic coordinates: 4114569-4115579.

## Biological Role

Repressed by glpR (protein.P0ACL0).

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

- `encodes` --> [[protein.P0A9C9|protein.P0A9C9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `S` - regulator=GlpR; target=glpX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012821,ECOCYC:EG11517,GeneID:948424`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4114569-4115579:-; feature_type=gene
