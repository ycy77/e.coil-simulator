---
entity_id: "gene.b3371"
entity_type: "gene"
name: "frlB"
source_database: "NCBI RefSeq"
source_id: "gene-b3371"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3371"
  - "frlB"
---

# frlB

`gene.b3371`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3371`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frlB (gene.b3371) is a gene entity. It encodes frlB (protein.P0AC00). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of fructoselysine 6-phosphate to glucose 6-phosphate and lysine (PubMed:12147680). Functions in a fructoselysine degradation pathway that allows E.coli to grow on fructoselysine or psicoselysine (PubMed:14641112). {ECO:0000269|PubMed:12147680, ECO:0000269|PubMed:14641112}. EcoCyc product frame: G7723-MONOMER. EcoCyc synonyms: yhfN. Genomic coordinates: 3501268-3502290. EcoCyc protein note: Fructoselysine 6-phosphate deglycase, which acts in fructoselysine degradation, is an FrlB dodecamer . The fructoselysine 6-phosphate deglycase reaction is reversible in vitro, but is catalyzed in the direction of formation of glucose 6-phosphate and lysine in vivo . A detailed reaction mechanism is discussed . Fructoselysine 6-phosphate deglycase activity is undetectable when cells are grown on glucose; stationary phase extract of cells grown on fructoselysine or psicoselysine have a deglycase activity of 20 nmol/min per mg of protein . An frlA mutant is unable to grow on 20mM fructoselysine or psicoselysine as the sole source of carbon . FrlB: "fructoselysine"

## Biological Role

Repressed by frlR (protein.P45544).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC00|protein.P0AC00]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P45544|protein.P45544]] `RegulonDB` `C` - regulator=FrlR; target=frlB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011021,ECOCYC:G7723,GeneID:947875`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3501268-3502290:+; feature_type=gene
