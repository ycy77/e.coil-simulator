---
entity_id: "reaction.R02401"
entity_type: "reaction"
name: "glutarate-semialdehyde:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R02401"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02401"
---

# glutarate-semialdehyde:NAD+ oxidoreductase

`reaction.R02401`

## Static

- Type: `reaction`
- Source: `KEGG:R02401`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Oxopentanoate + NAD+ + H2O Glutarate + NADH + H+

## Biological Role

Catalyzed by gabD (protein.P25526). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), 5-Oxopentanoate (molecule.C03273). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glutarate (molecule.C00489).

## Annotation

5-Oxopentanoate + NAD+ + H2O <=> Glutarate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P25526|protein.P25526]] `KEGG` `database` - via EC:1.2.1.20
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00489|molecule.C00489]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C03273|molecule.C03273]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080

## External IDs

- `KEGG:R02401`

## Notes

EQUATION: C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
