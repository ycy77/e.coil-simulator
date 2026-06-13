---
entity_id: "reaction.R04958"
entity_type: "reaction"
name: "octanoyl-[acp]:NAD+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04958"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04958"
---

# octanoyl-[acp]:NAD+ trans-2-oxidoreductase

`reaction.R04958`

## Static

- Type: `reaction`
- Source: `KEGG:R04958`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Octanoyl-[acp] + NAD+ trans-Oct-2-enoyl-[acp] + NADH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NAD+ (molecule.C00003), Octanoyl-[acp] (molecule.C05752). Products: NADH (molecule.C00004), H+ (molecule.C00080), trans-Oct-2-enoyl-[acp] (molecule.C05751).

## Annotation

Octanoyl-[acp] + NAD+ <=> trans-Oct-2-enoyl-[acp] + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.9
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080
- `is_product_of` <-- [[molecule.C05751|molecule.C05751]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C05752|molecule.C05752]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080

## External IDs

- `KEGG:R04958`

## Notes

EQUATION: C05752 + C00003 <=> C05751 + C00004 + C00080
