---
entity_id: "gene.b2911"
entity_type: "gene"
name: "ssrS"
source_database: "NCBI RefSeq"
source_id: "gene-b2911"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2911"
  - "ssrS"
---

# ssrS

`gene.b2911`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2911`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssrS (gene.b2911) is a gene entity. EcoCyc product frame: 6S-RNA. EcoCyc synonyms: ssr. Genomic coordinates: 3055983-3056165.

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), stpA (protein.P0ACG1), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssrS; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ssrS; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ssrS; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ssrS; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=ssrS; function=-
- `represses` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `S` - regulator=StpA; target=ssrS; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=ssrS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009556,ECOCYC:EG30099,GeneID:947405`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3055983-3056165:+; feature_type=gene
