---
entity_id: "gene.b2328"
entity_type: "gene"
name: "mepA"
source_database: "NCBI RefSeq"
source_id: "gene-b2328"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2328"
  - "mepA"
---

# mepA

`gene.b2328`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2328`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mepA (gene.b2328) is a gene entity. It encodes mepA (protein.P0C0T5). Encoded protein function: FUNCTION: Murein endopeptidase that cleaves the D-alanyl-meso-2,6-diamino-pimelyl amide bond that connects peptidoglycan strands. Likely plays a role in the removal of murein from the sacculus and could also play a role in the integration of nascent murein strands into the sacculus. {ECO:0000269|PubMed:15292190}. EcoCyc product frame: EG10580-MONOMER. Genomic coordinates: 2445560-2446384.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0T5|protein.P0C0T5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007691,ECOCYC:EG10580,GeneID:946812`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2445560-2446384:-; feature_type=gene
