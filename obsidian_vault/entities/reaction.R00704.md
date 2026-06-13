---
entity_id: "reaction.R00704"
entity_type: "reaction"
name: "(R)-lactate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00704"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00704"
---

# (R)-lactate:NAD+ oxidoreductase

`reaction.R00704`

## Static

- Type: `reaction`
- Source: `KEGG:R00704`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-Lactate + NAD+ Pyruvate + NADH + H+

## Biological Role

Catalyzed by ldhA (protein.P52643). Substrates: NAD+ (molecule.C00003), (R)-Lactate (molecule.C00256). Products: NADH (molecule.C00004), Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

(R)-Lactate + NAD+ <=> Pyruvate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P52643|protein.P52643]] `KEGG` `database` - via EC:1.1.1.28
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080

## External IDs

- `KEGG:R00704`

## Notes

EQUATION: C00256 + C00003 <=> C00022 + C00004 + C00080
