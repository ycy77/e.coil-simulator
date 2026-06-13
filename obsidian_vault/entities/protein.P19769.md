---
entity_id: "protein.P19769"
entity_type: "protein"
name: "insK"
source_database: "UniProt"
source_id: "P19769"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insK dinS b3558 JW3528"
---

# insK

`protein.P19769`

## Static

- Type: `protein`
- Source: `UniProt:P19769`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the transposition of the insertion sequence IS150. InsB is one of three proteins coded for by the IS150 insertion element. Its function is unknown. The IS150 insertion element, which is found singly or in many copies in various E. coli isolates, codes for three proteins, InsA, InsB and InsAB . Although InsA is translated normally, both InsB and InsAB translation require -1 frameshifts. InsAB translation begins from the same start codon as InsA translation, but a -1 frameshift allows readthrough on the former InsA stop codon, yielding the much longer protein InsAB. InsB translation begins at an ATG within the InsA sequence, requiring a -1 frameshift to properly translate it. In vivo, InsB is generated at a much lower rate than InsA or InsAB. The frameshift that generates InsAB rather than InsA occurs about a third of the time. Disruption of a putative stem-loop region following the frameshift site reduces InsAB expression dramatically . InsAB is the transposase for the IS150 insertion element. Though a lack of InsB has no effect on the process, loss of separate InsA leads to a 5-fold increase in transposition of IS150. However, this lack of independent InsA also leads to a dramatic increase in generation of free circular and linear IS150 elements, suggesting InsA plays a role in preventing abortive transposition events...

## Annotation

FUNCTION: Involved in the transposition of the insertion sequence IS150.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3558|gene.b3558]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19769`
- `KEGG:ecj:JW3528;eco:b3558;ecoc:C3026_19290;`
- `GeneID:948081;`
- `GO:GO:0003677; GO:0006310; GO:0006974; GO:0015074; GO:0032196`

## Notes

Putative transposase InsK for insertion sequence element IS150
