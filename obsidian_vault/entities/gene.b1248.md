---
entity_id: "gene.b1248"
entity_type: "gene"
name: "yciU"
source_database: "NCBI RefSeq"
source_id: "gene-b1248"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1248"
  - "yciU"
---

# yciU

`gene.b1248`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1248`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciU (gene.b1248) is a gene entity. It encodes yciU (protein.P0A8L7). Encoded protein function: FUNCTION: May act as a double-stranded DNA (dsDNA) mimic. Probably regulates the activity of a dsDNA-binding protein. {ECO:0000255|HAMAP-Rule:MF_00680}. EcoCyc product frame: G6633-MONOMER. Genomic coordinates: 1306821-1307150. EcoCyc protein note: YciU was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase . In a large genetic interaction screen, yciU showed genetic interactions with a number of proteins involved in translation and ribosome biogenesis .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8L7|protein.P0A8L7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yciU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004184,ECOCYC:G6633,GeneID:945819`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1306821-1307150:-; feature_type=gene
