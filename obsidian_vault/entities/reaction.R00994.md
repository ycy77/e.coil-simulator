---
entity_id: "reaction.R00994"
entity_type: "reaction"
name: "(2R,3S)-3-methylmalate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00994"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00994"
---

# (2R,3S)-3-methylmalate:NAD+ oxidoreductase

`reaction.R00994`

## Static

- Type: `reaction`
- Source: `KEGG:R00994`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxobutanoate + CO2 + NADH + H+ D-erythro-3-Methylmalate + NAD+

## Biological Role

Catalyzed by leuB (protein.P30125). Substrates: NADH (molecule.C00004), CO2 (molecule.C00011), H+ (molecule.C00080), 2-Oxobutanoate (molecule.C00109). Products: NAD+ (molecule.C00003), D-erythro-3-Methylmalate (molecule.C06032).

## Annotation

2-Oxobutanoate + CO2 + NADH + H+ <=> D-erythro-3-Methylmalate + NAD+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P30125|protein.P30125]] `KEGG` `database` - via EC:1.1.1.85
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_product_of` <-- [[molecule.C06032|molecule.C06032]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_substrate_of` <-- [[molecule.C00109|molecule.C00109]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003

## External IDs

- `KEGG:R00994`

## Notes

EQUATION: C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
