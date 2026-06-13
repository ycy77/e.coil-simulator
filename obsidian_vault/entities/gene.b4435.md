---
entity_id: "gene.b4435"
entity_type: "gene"
name: "isrC"
source_database: "NCBI RefSeq"
source_id: "gene-b4435"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4435"
  - "isrC"
---

# isrC

`gene.b4435`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4435`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

isrC (gene.b4435) is a gene entity. EcoCyc product frame: IS102-RNA. EcoCyc synonyms: IS102. Genomic coordinates: 2071317-2071511.

## Biological Role

Repressed by oxyR (protein.P0ACQ4). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=isrC; function=+
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=isrC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0047255,ECOCYC:G0-8905,GeneID:2847691`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:2071317-2071511:+; feature_type=gene
