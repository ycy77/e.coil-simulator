---
entity_id: "gene.b0205"
entity_type: "gene"
name: "rrfH"
source_database: "NCBI RefSeq"
source_id: "gene-b0205"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0205"
  - "rrfH"
---

# rrfH

`gene.b0205`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0205`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rrfH (gene.b0205) is a gene entity. EcoCyc product frame: RRFH-RRNA. Genomic coordinates: 228756-228875.

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

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rrfH; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=rrfH; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rrfH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000686,ECOCYC:EG30076,GeneID:944898`
- `gbkey:Gene`
- `gene_biotype:rRNA`

## Notes

NC_000913.3:228756-228875:+; feature_type=gene
