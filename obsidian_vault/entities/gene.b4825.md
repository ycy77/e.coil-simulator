---
entity_id: "gene.b4825"
entity_type: "gene"
name: "aspX"
source_database: "NCBI RefSeq"
source_id: "gene-b4825"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4825"
  - "aspX"
---

# aspX

`gene.b4825`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4825`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aspX (gene.b4825) is a gene entity. EcoCyc product frame: RNA0-418. Genomic coordinates: 4366839-4366951.

## Biological Role

Repressed by narL (protein.P0AF28). Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aspX; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=aspX; function=-

## External IDs

- `Dbxref:ECOCYC:G0-17100,GeneID:71004579`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4366839-4366951:-; feature_type=gene
