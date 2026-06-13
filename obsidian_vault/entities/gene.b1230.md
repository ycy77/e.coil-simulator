---
entity_id: "gene.b1230"
entity_type: "gene"
name: "tyrV"
source_database: "NCBI RefSeq"
source_id: "gene-b1230"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1230"
  - "tyrV"
---

# tyrV

`gene.b1230`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1230`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrV (gene.b1230) is a gene entity. EcoCyc product frame: tyrV-tRNA. EcoCyc synonyms: tyrTbeta. Genomic coordinates: 1287244-1287328.

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tyrV; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=tyrV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004134,ECOCYC:EG30108,GeneID:945811`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:1287244-1287328:-; feature_type=gene
