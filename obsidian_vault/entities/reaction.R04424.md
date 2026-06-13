---
entity_id: "reaction.R04424"
entity_type: "reaction"
name: "(2S,3S)-2-hydroxybutane-1,2,3-tricarboxylate hydro-lyase [(Z)-but-2-ene-1,2,3-tricarboxylate-forming]"
source_database: "KEGG"
source_id: "R04424"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04424"
---

# (2S,3S)-2-hydroxybutane-1,2,3-tricarboxylate hydro-lyase [(Z)-but-2-ene-1,2,3-tricarboxylate-forming]

`reaction.R04424`

## Static

- Type: `reaction`
- Source: `KEGG:R04424`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Methylcitrate (Z)-But-2-ene-1,2,3-tricarboxylate + H2O

## Biological Role

Catalyzed by prpD (protein.P77243). Substrates: 2-Methylcitrate (molecule.C02225). Products: H2O (molecule.C00001), (Z)-But-2-ene-1,2,3-tricarboxylate (molecule.C04225).

## Annotation

2-Methylcitrate <=> (Z)-But-2-ene-1,2,3-tricarboxylate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77243|protein.P77243]] `KEGG` `database` - via EC:4.2.1.79
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02225 <=> C04225 + C00001
- `is_product_of` <-- [[molecule.C04225|molecule.C04225]] `KEGG` `database` - C02225 <=> C04225 + C00001
- `is_substrate_of` <-- [[molecule.C02225|molecule.C02225]] `KEGG` `database` - C02225 <=> C04225 + C00001

## External IDs

- `KEGG:R04424`

## Notes

EQUATION: C02225 <=> C04225 + C00001
