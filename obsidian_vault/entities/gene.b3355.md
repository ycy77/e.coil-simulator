---
entity_id: "gene.b3355"
entity_type: "gene"
name: "prkB"
source_database: "NCBI RefSeq"
source_id: "gene-b3355"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3355"
  - "prkB"
---

# prkB

`gene.b3355`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3355`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prkB (gene.b3355) is a gene entity. It encodes prkB (protein.P0AEX5). Encoded protein function: Probable phosphoribulokinase (PRK) (PRKase) (EC 2.7.1.19) (Phosphopentokinase) EcoCyc product frame: EG12365-MONOMER. EcoCyc synonyms: yhfF. Genomic coordinates: 3484490-3485359. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 19, 2020.

## Enriched Pathways

- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEX5|protein.P0AEX5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010962,ECOCYC:EG12365,GeneID:947862`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3484490-3485359:+; feature_type=gene
