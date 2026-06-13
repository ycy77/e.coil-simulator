---
entity_id: "protein.P0CF88"
entity_type: "protein"
name: "insI1"
source_database: "UniProt"
source_id: "P0CF88"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insI1 b0256 JW0246"
---

# insI1

`protein.P0CF88`

## Static

- Type: `protein`
- Source: `UniProt:P0CF88`
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

- `encodes` <-- [[gene.b0256|gene.b0256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CF88`
- `KEGG:ecj:JW0246;eco:b0256;ecoc:C3026_01225;ecoc:C3026_08185;ecoc:C3026_21990;ecoc:C3026_23960;`
- `GeneID:949005;`
- `GO:GO:0004803; GO:0006313; GO:0015074; GO:0032135; GO:0032196; GO:0032993; GO:0043565`

## Notes

Transposase InsI for insertion sequence element IS30A
