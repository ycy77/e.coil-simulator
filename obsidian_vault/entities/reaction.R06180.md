---
entity_id: "reaction.R06180"
entity_type: "reaction"
name: "R06180"
source_database: "KEGG"
source_id: "R06180"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06180"
---

# R06180

`reaction.R06180`

## Static

- Type: `reaction`
- Source: `KEGG:R06180`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R,R)-Tartaric acid + NAD+ 2-Hydroxy-3-oxosuccinate + NADH + H+

## Biological Role

Catalyzed by dmlA (protein.P76251). Substrates: NAD+ (molecule.C00003), (R,R)-Tartaric acid (molecule.C00898). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2-Hydroxy-3-oxosuccinate (molecule.C03459).

## Annotation

(R,R)-Tartaric acid + NAD+ <=> 2-Hydroxy-3-oxosuccinate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76251|protein.P76251]] `KEGG` `database` - via EC:1.1.1.93
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_product_of` <-- [[molecule.C03459|molecule.C03459]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00898|molecule.C00898]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080

## External IDs

- `KEGG:R06180`

## Notes

EQUATION: C00898 + C00003 <=> C03459 + C00004 + C00080
