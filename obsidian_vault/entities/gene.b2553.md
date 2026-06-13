---
entity_id: "gene.b2553"
entity_type: "gene"
name: "glnB"
source_database: "NCBI RefSeq"
source_id: "gene-b2553"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2553"
  - "glnB"
---

# glnB

`gene.b2553`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2553`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnB (gene.b2553) is a gene entity. It encodes glnB (protein.P0A9Z1). Encoded protein function: FUNCTION: P-II indirectly controls the transcription of the glutamine synthetase gene (glnA). P-II prevents NR-II-catalyzed conversion of NR-I to NR-I-phosphate, the transcriptional activator of GlnA. When P-II is uridylylated to P-II-UMP, these events are reversed. When the ratio of Gln to 2-ketoglutarate decreases, P-II is uridylylated to P-II-UMP, which causes the deadenylation of glutamine synthetase by GlnE, so activating the enzyme. EcoCyc product frame: URIDYLYL-PII. Genomic coordinates: 2687070-2687408.

## Biological Role

Repressed by purR (protein.P0ACP7).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9Z1|protein.P0A9Z1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=glnB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008398,ECOCYC:EG10384,GeneID:947016`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2687070-2687408:-; feature_type=gene
