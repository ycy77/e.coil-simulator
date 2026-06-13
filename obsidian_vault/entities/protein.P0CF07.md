---
entity_id: "protein.P0CF07"
entity_type: "protein"
name: "insA1"
source_database: "UniProt"
source_id: "P0CF07"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insA1 b0022 JW0021"
---

# insA1

`protein.P0CF07`

## Static

- Type: `protein`
- Source: `UniProt:P0CF07`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Absolutely required for transposition of IS1. IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

FUNCTION: Absolutely required for transposition of IS1.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0022|gene.b0022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CF07`
- `KEGG:ecj:JW0021;eco:b0022;eco:b1894;eco:b3444;ecoc:C3026_00105;`
- `GeneID:948449;`
- `GO:GO:0006313`

## Notes

Insertion element IS1 1 protein InsA (IS1a)
