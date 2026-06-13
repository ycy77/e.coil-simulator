---
entity_id: "gene.b4431"
entity_type: "gene"
name: "rprA"
source_database: "NCBI RefSeq"
source_id: "gene-b4431"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4431"
  - "rprA"
---

# rprA

`gene.b4431`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4431`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rprA (gene.b4431) is a gene entity. EcoCyc product frame: RPRA-RNA. EcoCyc synonyms: psrA5, IS083. Genomic coordinates: 1770372-1770477.

## Biological Role

Activated by cpxR (protein.P0AE88), rcsB (protein.P0DMC7).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (7)

- `activates` --> [[gene.b2741|gene.b2741]] `RegulonDB` `S` - regulator=RprA; target=rpoS; function=+
- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=RprA; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=RprA; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=RprA; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=RprA; target=csgD; function=-
- `represses` --> [[gene.b1341|gene.b1341]] `RegulonDB` `S` - regulator=RprA; target=dgcM; function=-
- `represses` --> [[gene.b2193|gene.b2193]] `RegulonDB` `S` - regulator=RprA; target=narP; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=rprA; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `S` - regulator=RcsB; target=rprA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047251,ECOCYC:G0-8863,GeneID:2847671`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:1770372-1770477:+; feature_type=gene
