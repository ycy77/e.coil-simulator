---
entity_id: "gene.b3176"
entity_type: "gene"
name: "glmM"
source_database: "NCBI RefSeq"
source_id: "gene-b3176"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3176"
  - "glmM"
---

# glmM

`gene.b3176`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3176`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glmM (gene.b3176) is a gene entity. It encodes glmM (protein.P31120). Encoded protein function: FUNCTION: Catalyzes the conversion of glucosamine-6-phosphate to glucosamine-1-phosphate. Can also catalyze the formation of glucose-6-P from glucose-1-P, although at a 1400-fold lower rate. {ECO:0000269|PubMed:10231382}. EcoCyc product frame: PHOSGLUCOSAMINEMUT-MONOMER. EcoCyc synonyms: yhbF, mrsA. Genomic coordinates: 3322733-3324070.

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31120|protein.P31120]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010439,ECOCYC:EG11553,GeneID:947692`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3322733-3324070:-; feature_type=gene
