---
entity_id: "gene.b4474"
entity_type: "gene"
name: "frlC"
source_database: "NCBI RefSeq"
source_id: "gene-b4474"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4474"
  - "frlC"
---

# frlC

`gene.b4474`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4474`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frlC (gene.b4474) is a gene entity. It encodes frlC (protein.P45541). Encoded protein function: FUNCTION: Catalyzes the reversible interconversion of fructoselysine with its C-3 epimer, psicoselysine. Allows E.coli to utilize psicoselysine for growth. Does not act on psicose or fructoselysine 6-phosphate. {ECO:0000269|PubMed:14641112}. EcoCyc product frame: G7724-MONOMER. EcoCyc synonyms: b3373, yhfP, yhfO, b3372. Genomic coordinates: 3502340-3503170. EcoCyc protein note: Fructoselysine 3-epimerase catalyzes the interconversion of fructoselysine and psicoselysine . Fructoselysine 3-epimerase activity is undetectable when cells are grown on glucose; stationary phase extract of cells grown on fructoselysine or psicoselysine have an epimerase activity of 2 nmol/min per mg of protein . FrlC: "fructoselysine"

## Biological Role

Repressed by frlR (protein.P45544).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45541|protein.P45541]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P45544|protein.P45544]] `RegulonDB` `C` - regulator=FrlR; target=frlC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174114,ECOCYC:G7724,GeneID:2847758`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3502340-3503170:+; feature_type=gene
