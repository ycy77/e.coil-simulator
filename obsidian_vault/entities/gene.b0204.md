---
entity_id: "gene.b0204"
entity_type: "gene"
name: "rrlH"
source_database: "NCBI RefSeq"
source_id: "gene-b0204"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0204"
  - "rrlH"
---

# rrlH

`gene.b0204`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0204`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrlH (gene.b0204) is a gene entity. EcoCyc product frame: RRLH-RRNA. Genomic coordinates: 225759-228662.

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrlH; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrlH; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrlH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000684,ECOCYC:EG30083,GeneID:944900`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:225759-228662:+; feature_type=gene
