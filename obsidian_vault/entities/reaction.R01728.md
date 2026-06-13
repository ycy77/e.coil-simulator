---
entity_id: "reaction.R01728"
entity_type: "reaction"
name: "prephenate:NAD+ oxidoreductase(decarboxylating)"
source_database: "KEGG"
source_id: "R01728"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01728"
---

# prephenate:NAD+ oxidoreductase(decarboxylating)

`reaction.R01728`

## Static

- Type: `reaction`
- Source: `KEGG:R01728`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Prephenate + NAD+ 3-(4-Hydroxyphenyl)pyruvate + CO2 + NADH + H+

## Biological Role

Catalyzed by tyrA (protein.P07023). Substrates: NAD+ (molecule.C00003), Prephenate (molecule.C00254). Products: NADH (molecule.C00004), CO2 (molecule.C00011), H+ (molecule.C00080), 3-(4-Hydroxyphenyl)pyruvate (molecule.C01179).

## Annotation

Prephenate + NAD+ <=> 3-(4-Hydroxyphenyl)pyruvate + CO2 + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07023|protein.P07023]] `KEGG` `database` - via EC:1.3.1.12
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_product_of` <-- [[molecule.C01179|molecule.C01179]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080

## External IDs

- `KEGG:R01728`

## Notes

EQUATION: C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
