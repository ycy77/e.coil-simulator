---
entity_id: "gene.b1380"
entity_type: "gene"
name: "ldhA"
source_database: "NCBI RefSeq"
source_id: "gene-b1380"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1380"
  - "ldhA"
---

# ldhA

`gene.b1380`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1380`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldhA (gene.b1380) is a gene entity. It encodes ldhA (protein.P52643). Encoded protein function: FUNCTION: Fermentative lactate dehydrogenase. {ECO:0000269|PubMed:4297265}. EcoCyc product frame: DLACTDEHYDROGNAD-MONOMER. EcoCyc synonyms: htpH, hslF, hslI. Genomic coordinates: 1441854-1442843.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52643|protein.P52643]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004619,ECOCYC:G592,GeneID:946315`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1441854-1442843:-; feature_type=gene
