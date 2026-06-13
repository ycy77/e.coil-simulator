---
entity_id: "gene.b1236"
entity_type: "gene"
name: "galU"
source_database: "NCBI RefSeq"
source_id: "gene-b1236"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1236"
  - "galU"
---

# galU

`gene.b1236`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1236`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galU (gene.b1236) is a gene entity. It encodes galU (protein.P0AEP3). Encoded protein function: FUNCTION: May play a role in stationary phase survival. EcoCyc product frame: GLUC1PURIDYLTRANS-MONOMER. EcoCyc synonyms: ychD. Genomic coordinates: 1291457-1292365.

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEP3|protein.P0AEP3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004150,ECOCYC:EG11319,GeneID:945730`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1291457-1292365:+; feature_type=gene
