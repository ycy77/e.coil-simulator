---
entity_id: "gene.b3273"
entity_type: "gene"
name: "thrV"
source_database: "NCBI RefSeq"
source_id: "gene-b3273"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3273"
  - "thrV"
---

# thrV

`gene.b3273`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3273`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrV (gene.b3273) is a gene entity. EcoCyc product frame: thrV-tRNA. Genomic coordinates: 3423580-3423655.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=thrV; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=thrV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010742,ECOCYC:EG30103,GeneID:947770`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3423580-3423655:-; feature_type=gene
