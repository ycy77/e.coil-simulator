---
entity_id: "reaction.R04425"
entity_type: "reaction"
name: "(2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate hydro-lyase"
source_database: "KEGG"
source_id: "R04425"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04425"
---

# (2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate hydro-lyase

`reaction.R04425`

## Static

- Type: `reaction`
- Source: `KEGG:R04425`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate (Z)-But-2-ene-1,2,3-tricarboxylate + H2O

## Biological Role

Catalyzed by acnA (protein.P25516), acnB (protein.P36683). Substrates: (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate (molecule.C04593). Products: H2O (molecule.C00001), (Z)-But-2-ene-1,2,3-tricarboxylate (molecule.C04225).

## Annotation

(2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate <=> (Z)-But-2-ene-1,2,3-tricarboxylate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25516|protein.P25516]] `KEGG` `database` - via EC:4.2.1.99
- `catalyzes` <-- [[protein.P36683|protein.P36683]] `KEGG` `database` - via EC:4.2.1.99
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04593 <=> C04225 + C00001
- `is_product_of` <-- [[molecule.C04225|molecule.C04225]] `KEGG` `database` - C04593 <=> C04225 + C00001
- `is_substrate_of` <-- [[molecule.C04593|molecule.C04593]] `KEGG` `database` - C04593 <=> C04225 + C00001

## External IDs

- `KEGG:R04425`

## Notes

EQUATION: C04593 <=> C04225 + C00001
