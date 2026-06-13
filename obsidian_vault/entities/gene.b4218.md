---
entity_id: "gene.b4218"
entity_type: "gene"
name: "paeA"
source_database: "NCBI RefSeq"
source_id: "gene-b4218"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4218"
  - "paeA"
---

# paeA

`gene.b4218`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4218`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paeA (gene.b4218) is a gene entity. It encodes paeA (protein.P0AE45). Encoded protein function: FUNCTION: Involved in cadaverine and putrescine tolerance in stationary phase. May facilitate the efflux of both cadaverine and putrescine from the cytoplasm, reducing potentially toxic levels under certain stress conditions. {ECO:0000269|PubMed:33481283}. EcoCyc product frame: G7873-MONOMER. EcoCyc synonyms: ytfL. Genomic coordinates: 4439872-4441215. EcoCyc protein note: PaeA (formerly YtfL) is predicted to be an inner membrane protein with four transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . A paeA deletion mutant (ΔpaeA::kan) is more sensitive to nalidixic acid and kasugamycin than wild type . PaeA is implicated in the selective efflux of cadaverine and putrescine in Salmonella Typhimurium and is important for stationary phase survival when cells are grown in acidic medium; deletion of paeA in E. coli K-12 increases sensitivity to cadaverine and putrescine but not to spermidine and spermine . paeA: polyamine export

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE45|protein.P0AE45]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013799,ECOCYC:G7873,GeneID:948735`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4439872-4441215:-; feature_type=gene
