---
entity_id: "gene.b4433"
entity_type: "gene"
name: "sdsR"
source_database: "NCBI RefSeq"
source_id: "gene-b4433"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4433"
  - "sdsR"
---

# sdsR

`gene.b4433`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4433`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdsR (gene.b4433) is a gene entity. EcoCyc product frame: RYEB-RNA. EcoCyc synonyms: tkpe79, ryeB. Genomic coordinates: 1923104-1923207.

## Biological Role

Activated by rpoH (protein.P0AGB3), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (4)

- `represses` --> [[gene.b1783|gene.b1783]] `RegulonDB` `S` - regulator=SdsR; target=yeaG; function=-
- `represses` --> [[gene.b1784|gene.b1784]] `RegulonDB` `S` - regulator=SdsR; target=yeaH; function=-
- `represses` --> [[gene.b3035|gene.b3035]] `RegulonDB` `S` - regulator=SdsR; target=tolC; function=-
- `represses` --> [[gene.b3233|gene.b3233]] `RegulonDB` `S` - regulator=SdsR; target=yhcB; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=sdsR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sdsR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047253,ECOCYC:G0-8883,GeneID:2847772`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1923104-1923207:-; feature_type=gene
