---
entity_id: "reaction.R11945"
entity_type: "reaction"
name: "NADH:ubiquinone oxidoreductase"
source_database: "KEGG"
source_id: "R11945"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11945"
---

# NADH:ubiquinone oxidoreductase

`reaction.R11945`

## Static

- Type: `reaction`
- Source: `KEGG:R11945`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ubiquinone + NADH + H+ + 4 H+ Ubiquinol + NAD+ + 4 H+

## Biological Role

Catalyzed by nuoA (protein.P0AFC3), nuoB (protein.P0AFC7), nuoE (protein.P0AFD1), nuoH (protein.P0AFD4), nuoI (protein.P0AFD6), nuoJ (protein.P0AFE0), nuoK (protein.P0AFE4), nuoM (protein.P0AFE8), and 5 more. Substrates: NADH (molecule.C00004), H+ (molecule.C00080), Ubiquinone (molecule.C00399). Products: NAD+ (molecule.C00003), H+ (molecule.C00080), Ubiquinol (molecule.C00390).

## Annotation

Ubiquinone + NADH + H+ + 4 H+ <=> Ubiquinol + NAD+ + 4 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `catalyzes` <-- [[protein.P0AFC3|protein.P0AFC3]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFC7|protein.P0AFC7]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFD1|protein.P0AFD1]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFD4|protein.P0AFD4]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFD6|protein.P0AFD6]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFE0|protein.P0AFE0]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFE4|protein.P0AFE4]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFE8|protein.P0AFE8]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P0AFF0|protein.P0AFF0]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P31979|protein.P31979]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P33599|protein.P33599]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P33602|protein.P33602]] `KEGG` `database` - via EC:7.1.1.2
- `catalyzes` <-- [[protein.P33607|protein.P33607]] `KEGG` `database` - via EC:7.1.1.2
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_substrate_of` <-- [[molecule.C00399|molecule.C00399]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080

## External IDs

- `KEGG:R11945`

## Notes

EQUATION: C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
