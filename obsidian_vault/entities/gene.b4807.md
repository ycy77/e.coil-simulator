---
entity_id: "gene.b4807"
entity_type: "gene"
name: "malH"
source_database: "NCBI RefSeq"
source_id: "gene-b4807"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4807"
  - "malH"
---

# malH

`gene.b4807`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4807`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malH (gene.b4807) is a gene entity. EcoCyc product frame: RNA0-410. Genomic coordinates: 4242531-4242633.

## Biological Role

Activated by rpoD (protein.P00579), malT (protein.P06993), fis (protein.P0A6R3), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malH; function=+
- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malH; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=malH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malH; function=+

## External IDs

- `Dbxref:ECOCYC:G0-17082,GeneID:71004577`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4242531-4242633:-; feature_type=gene
