---
entity_id: "gene.b0517"
entity_type: "gene"
name: "allD"
source_database: "NCBI RefSeq"
source_id: "gene-b0517"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0517"
  - "allD"
---

# allD

`gene.b0517`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0517`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allD (gene.b0517) is a gene entity. It encodes allD (protein.P77555). Encoded protein function: FUNCTION: AllD plays a pivotal role as a metabolic branch-point enzyme in nitrogen utilization via the assimilation of allantoin (PubMed:10601204). It is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions (PubMed:10601204). Catalyzes the oxidation of ureidoglycolate to oxalurate (PubMed:23284870). {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:23284870}. EcoCyc product frame: G6286-MONOMER. EcoCyc synonyms: glxB8, ylbC. Genomic coordinates: 545314-546363.

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77555|protein.P77555]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001780,ECOCYC:G6286,GeneID:948342`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:545314-546363:-; feature_type=gene
