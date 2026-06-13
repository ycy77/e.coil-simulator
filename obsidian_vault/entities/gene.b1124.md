---
entity_id: "gene.b1124"
entity_type: "gene"
name: "potC"
source_database: "NCBI RefSeq"
source_id: "gene-b1124"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1124"
  - "potC"
---

# potC

`gene.b1124`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1124`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potC (gene.b1124) is a gene entity. It encodes potC (protein.P0AFK6). Encoded protein function: FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. EcoCyc product frame: POTC-MONOMER. Genomic coordinates: 1182826-1183620. EcoCyc protein note: potC encodes one of two integral membrane subunits of an ATP-dependent spermidine uptake system; PotC is predicted to contain 6 transmembrane regions

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFK6|protein.P0AFK6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003791,ECOCYC:EG10751,GeneID:945691`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1182826-1183620:-; feature_type=gene
