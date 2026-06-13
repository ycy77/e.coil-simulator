---
entity_id: "protein.P0CF90"
entity_type: "protein"
name: "insI4"
source_database: "UniProt"
source_id: "P0CF90"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insI4 b4284 JW4244"
---

# insI4

`protein.P0CF90`

## Static

- Type: `protein`
- Source: `UniProt:P0CF90`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for the transposition of the insertion element. {ECO:0000305}. This is the transposase for the insertion sequence IS30. The IS30 transposase interacts with the terminal inverted repeats of the IS30 sequence element, using them as targets for transposition . The carboxy-terminus of the transposase is required for formation and dissolution of the dimeric transpositional intermediate .

## Biological Role

Catalyzes RXN0-5131 (reaction.ecocyc.RXN0-5131).

## Annotation

FUNCTION: Required for the transposition of the insertion element. {ECO:0000305}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5131|reaction.ecocyc.RXN0-5131]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4284|gene.b4284]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CF90`
- `KEGG:ecj:JW4244;eco:b1404;eco:b4284;ecoc:C3026_23100;`
- `GeneID:93673411;`
- `GO:GO:0003677; GO:0004803; GO:0006313; GO:0015074; GO:0032196`

## Notes

Transposase InsI for insertion sequence element IS30D
