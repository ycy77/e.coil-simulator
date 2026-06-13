---
entity_id: "gene.b4716"
entity_type: "gene"
name: "cpxQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4716"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4716"
  - "cpxQ"
---

# cpxQ

`gene.b4716`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4716`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpxQ (gene.b4716) is a gene entity. EcoCyc product frame: RNA0-389. Genomic coordinates: 4106330-4106387.

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `represses` --> [[gene.b1661|gene.b1661]] `RegulonDB` `S` - regulator=CpxQ; target=cfa; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=cpxQ; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `C` - regulator=CpxR; target=cpxQ; function=+

## External IDs

- `Dbxref:ECOCYC:G0-16649,GeneID:38094976`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:4106330-4106387:+; feature_type=gene
