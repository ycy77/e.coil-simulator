---
entity_id: "gene.b1607"
entity_type: "gene"
name: "ydgC"
source_database: "NCBI RefSeq"
source_id: "gene-b1607"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1607"
  - "ydgC"
---

# ydgC

`gene.b1607`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1607`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydgC (gene.b1607) is a gene entity. It encodes ydgC (protein.P0ACX0). Encoded protein function: Inner membrane protein YdgC EcoCyc product frame: G6863-MONOMER. Genomic coordinates: 1681695-1682030. EcoCyc protein note: YdgC may be a dual-topology protein which forms an antiparallel homodimer or higher order oligomer within the membrane; the protein contains four predicted transmembrane domains and has very weak topology bias; the C-terminal orientation of the protein is highly sensitive to charge mutations .

## Biological Role

Repressed by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACX0|protein.P0ACX0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=ydgC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005366,ECOCYC:G6863,GeneID:945156`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1681695-1682030:-; feature_type=gene
