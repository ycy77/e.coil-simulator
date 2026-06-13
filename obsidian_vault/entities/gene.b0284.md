---
entity_id: "gene.b0284"
entity_type: "gene"
name: "paoC"
source_database: "NCBI RefSeq"
source_id: "gene-b0284"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0284"
  - "paoC"
---

# paoC

`gene.b0284`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0284`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paoC (gene.b0284) is a gene entity. It encodes paoC (protein.P77489). Encoded protein function: FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}. EcoCyc product frame: G6155-MONOMER. EcoCyc synonyms: yagR. Genomic coordinates: 298736-300934. EcoCyc protein note: paoC encodes the large, molybdenum cofactor-containing subunit of a heterotrimeric periplasmic aldehyde oxidoreductase, PaoABC . A paoC single deletion mutant is unable to grow in the presence of cinnamaldehyde at pH 4.0 .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77489|protein.P77489]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000988,ECOCYC:G6155,GeneID:944961`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:298736-300934:-; feature_type=gene
