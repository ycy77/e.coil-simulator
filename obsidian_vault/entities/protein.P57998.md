---
entity_id: "protein.P57998"
entity_type: "protein"
name: "insB4"
source_database: "UniProt"
source_id: "P57998"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insB4 b0988 JW0972"
---

# insB4

`protein.P57998`

## Static

- Type: `protein`
- Source: `UniProt:P57998`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Absolutely required for transposition of IS1. IS1 is the smallest insertion sequence in E. coli. It codes for three proteins, InsA, InsB and InsAB'. InsAB' is the transposase for IS1 . Its translation depends on a -1 frameshift within the 3' end region of insA which allows translational readthrough into insB . In the absence of this frameshift, the IS1 transcriptional repressor protein InsA is produced instead .

## Annotation

FUNCTION: Absolutely required for transposition of IS1.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0988|gene.b0988]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P57998`
- `KEGG:ecj:JW0972;eco:b0988;ecoc:C3026_06025;`
- `GeneID:945009;`
- `GO:GO:0003677; GO:0004803; GO:0006313`

## Notes

Insertion element IS1 4 protein InsB (IS1d)
