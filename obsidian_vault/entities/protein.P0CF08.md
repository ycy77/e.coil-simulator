---
entity_id: "protein.P0CF08"
entity_type: "protein"
name: "insA2"
source_database: "UniProt"
source_id: "P0CF08"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insA2 b0265 JW0257"
---

# insA2

`protein.P0CF08`

## Static

- Type: `protein`
- Source: `UniProt:P0CF08`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Absolutely required for transposition of IS1. IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

FUNCTION: Absolutely required for transposition of IS1.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0265|gene.b0265]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CF08`
- `KEGG:ecj:JW0257;eco:b0265;eco:b0275;eco:b4516;ecoc:C3026_01280;`
- `GeneID:944946;`
- `GO:GO:0006313`

## Notes

Insertion element IS1 2 protein InsA (IS1b)
