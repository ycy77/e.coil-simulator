---
entity_id: "gene.b2020"
entity_type: "gene"
name: "hisD"
source_database: "NCBI RefSeq"
source_id: "gene-b2020"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2020"
  - "hisD"
---

# hisD

`gene.b2020`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2020`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisD (gene.b2020) is a gene entity. It encodes hisD (protein.P06988). Encoded protein function: FUNCTION: Catalyzes the sequential NAD-dependent oxidations of L-histidinol to L-histidinaldehyde and then to L-histidine. {ECO:0000255|HAMAP-Rule:MF_01024}. EcoCyc product frame: HISTDEHYD-MONOMER. Genomic coordinates: 2091097-2092401.

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06988|protein.P06988]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006715,ECOCYC:EG10447,GeneID:946531`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2091097-2092401:+; feature_type=gene
