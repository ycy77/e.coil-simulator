---
entity_id: "gene.b2267"
entity_type: "gene"
name: "elaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2267"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2267"
  - "elaA"
---

# elaA

`gene.b2267`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2267`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elaA (gene.b2267) is a gene entity. It encodes elaA (protein.P0AEH3). Encoded protein function: Protein ElaA EcoCyc product frame: G7174-MONOMER. EcoCyc synonyms: yfbC. Genomic coordinates: 2381082-2381543. EcoCyc protein note: Overexpression of elaA from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEH3|protein.P0AEH3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007489,ECOCYC:G7174,GeneID:946750`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2381082-2381543:-; feature_type=gene
