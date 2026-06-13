---
entity_id: "gene.b0202"
entity_type: "gene"
name: "ileV"
source_database: "NCBI RefSeq"
source_id: "gene-b0202"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0202"
  - "ileV"
---

# ileV

`gene.b0202`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0202`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ileV (gene.b0202) is a gene entity. EcoCyc product frame: ileV-tRNA. Genomic coordinates: 225381-225457.

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ileV; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ileV; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ileV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000679,ECOCYC:EG30045,GeneID:944884`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:225381-225457:+; feature_type=gene
