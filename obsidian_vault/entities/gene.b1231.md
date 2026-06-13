---
entity_id: "gene.b1231"
entity_type: "gene"
name: "tyrT"
source_database: "NCBI RefSeq"
source_id: "gene-b1231"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1231"
  - "tyrT"
---

# tyrT

`gene.b1231`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1231`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrT (gene.b1231) is a gene entity. EcoCyc product frame: tyrT-tRNA. EcoCyc synonyms: tyrTalpha, supFsupO, Su-3, Su-4, su(c), suIII, supC. Genomic coordinates: 1287538-1287622.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tyrT; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=tyrT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004136,ECOCYC:EG30106,GeneID:945820`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:1287538-1287622:-; feature_type=gene
