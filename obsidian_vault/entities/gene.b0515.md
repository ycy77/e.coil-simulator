---
entity_id: "gene.b0515"
entity_type: "gene"
name: "allE"
source_database: "NCBI RefSeq"
source_id: "gene-b0515"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0515"
  - "allE"
---

# allE

`gene.b0515`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0515`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allE (gene.b0515) is a gene entity. It encodes allE (protein.P75713). Encoded protein function: FUNCTION: Involved in the anaerobic nitrogen utilization via the assimilation of allantoin. Catalyzes the second stereospecific hydrolysis reaction (deamination) of the allantoin degradation pathway, producing S-ureidoglycolate and ammonia from S-ureidoglycine. {ECO:0000269|PubMed:19935661, ECO:0000269|PubMed:20038185}. EcoCyc product frame: G6284-MONOMER. EcoCyc synonyms: glxB6, ylbA, ughY. Genomic coordinates: 543261-544046. EcoCyc protein note: (S)-ureidoglycine aminohydrolase catalyzes the second, stereospecific hydrolysis reaction of the allantoin degradation pathway, producing CPD-1091 and ammonia from CPD0-2298 . Although hydrolysis of ureidoglycine can proceed spontaneously, the spontaneous reaction appears to be slow and not stereospecific . UghY: "(S)-ureidoglycine aminohydrolase"

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75713|protein.P75713]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001775,ECOCYC:G6284,GeneID:945149`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:543261-544046:-; feature_type=gene
