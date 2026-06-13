---
entity_id: "protein.P0CF26"
entity_type: "protein"
name: "insB2"
source_database: "UniProt"
source_id: "P0CF26"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insB2 b0264 JW0256"
---

# insB2

`protein.P0CF26`

## Static

- Type: `protein`
- Source: `UniProt:P0CF26`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Absolutely required for transposition of IS1. IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

FUNCTION: Absolutely required for transposition of IS1.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0264|gene.b0264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CF26`
- `KEGG:ecj:JW0256;eco:b0264;eco:b0274;ecoc:C3026_01275;ecoc:C3026_01330;`
- `GeneID:947698;`
- `GO:GO:0003677; GO:0004803; GO:0006313`

## Notes

Insertion element IS1 2 protein InsB (IS1b)
