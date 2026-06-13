---
entity_id: "gene.b3076"
entity_type: "gene"
name: "ebgA"
source_database: "NCBI RefSeq"
source_id: "gene-b3076"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3076"
  - "ebgA"
---

# ebgA

`gene.b3076`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3076`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ebgA (gene.b3076) is a gene entity. It encodes ebgA (protein.P06864). Encoded protein function: FUNCTION: The wild-type enzyme is an ineffective lactase. Two classes of point mutations dramatically improve activity of the enzyme. EcoCyc product frame: EG10252-MONOMER. Genomic coordinates: 3222633-3225725.

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06864|protein.P06864]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010104,ECOCYC:EG10252,GeneID:947583`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3222633-3225725:+; feature_type=gene
