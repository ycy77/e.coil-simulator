---
entity_id: "gene.b3276"
entity_type: "gene"
name: "alaU"
source_database: "NCBI RefSeq"
source_id: "gene-b3276"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3276"
  - "alaU"
---

# alaU

`gene.b3276`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3276`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alaU (gene.b3276) is a gene entity. EcoCyc product frame: alaU-tRNA. EcoCyc synonyms: talD. Genomic coordinates: 3426958-3427033.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alaU; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=alaU; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=alaU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010748,ECOCYC:EG30009,GeneID:947772`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3426958-3427033:-; feature_type=gene
