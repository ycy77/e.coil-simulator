---
entity_id: "gene.b0516"
entity_type: "gene"
name: "allC"
source_database: "NCBI RefSeq"
source_id: "gene-b0516"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0516"
  - "allC"
---

# allC

`gene.b0516`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0516`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allC (gene.b0516) is a gene entity. It encodes allC (protein.P77425). Encoded protein function: FUNCTION: Involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:10601204, PubMed:20038185). Catalyzes specifically the hydrolysis of allantoate to yield CO2, NH3 and S-ureidoglycine, which is unstable and readily undergoes a second deamination by S-ureidoglycine aminohydrolase AllE to yield S-ureidoglycolate and NH3 (PubMed:20038185). In vivo, the spontaneous release of S-ureidoglycolate and ammonia from S-ureidoglycine appears to be too slow to sustain an efficient flux of nitrogen (PubMed:20038185). {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:20038185}. EcoCyc product frame: G6285-MONOMER. EcoCyc synonyms: glxB7, ylbB. Genomic coordinates: 544057-545292.

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77425|protein.P77425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001777,ECOCYC:G6285,GeneID:945150`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:544057-545292:-; feature_type=gene
