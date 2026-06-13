---
entity_id: "gene.b2172"
entity_type: "gene"
name: "yeiQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2172"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2172"
  - "yeiQ"
---

# yeiQ

`gene.b2172`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2172`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiQ (gene.b2172) is a gene entity. It encodes yeiQ (protein.P33029). Encoded protein function: Uncharacterized oxidoreductase YeiQ (EC 1.-.-.-) EcoCyc product frame: EG12036-MONOMER. Genomic coordinates: 2266245-2267711. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 19, 2019.

## Biological Role

Repressed by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33029|protein.P33029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yeiQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007191,ECOCYC:EG12036,GeneID:946688`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2266245-2267711:+; feature_type=gene
