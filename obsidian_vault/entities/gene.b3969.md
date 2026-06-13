---
entity_id: "gene.b3969"
entity_type: "gene"
name: "gltT"
source_database: "NCBI RefSeq"
source_id: "gene-b3969"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3969"
  - "gltT"
---

# gltT

`gene.b3969`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3969`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltT (gene.b3969) is a gene entity. EcoCyc product frame: gltT-tRNA. EcoCyc synonyms: tgtB. Genomic coordinates: 4168372-4168447.

## Biological Role

Repressed by hns (protein.P0ACF8), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gltT; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=gltT; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=gltT; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gltT; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gltT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012993,ECOCYC:EG30032,GeneID:948465`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4168372-4168447:+; feature_type=gene
