---
entity_id: "reaction.R00196"
entity_type: "reaction"
name: "(S)-lactate:ferricytochrome-c 2-oxidoreductase"
source_database: "KEGG"
source_id: "R00196"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00196"
---

# (S)-lactate:ferricytochrome-c 2-oxidoreductase

`reaction.R00196`

## Static

- Type: `reaction`
- Source: `KEGG:R00196`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Lactate + 2 Ferricytochrome c Pyruvate + 2 Ferrocytochrome c + 2 H+

## Biological Role

Catalyzed by lldD (protein.P33232). Substrates: (S)-Lactate (molecule.C00186). Products: Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

(S)-Lactate + 2 Ferricytochrome c <=> Pyruvate + 2 Ferrocytochrome c + 2 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P33232|protein.P33232]] `KEGG` `database` - via EC:1.1.2.3
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00186 + 2 C00125 <=> C00022 + 2 C00126 + 2 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00186 + 2 C00125 <=> C00022 + 2 C00126 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00186|molecule.C00186]] `KEGG` `database` - C00186 + 2 C00125 <=> C00022 + 2 C00126 + 2 C00080

## External IDs

- `KEGG:R00196`

## Notes

EQUATION: C00186 + 2 C00125 <=> C00022 + 2 C00126 + 2 C00080
