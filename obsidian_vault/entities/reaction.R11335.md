---
entity_id: "reaction.R11335"
entity_type: "reaction"
name: "ubiquinol:oxygen oxidoreductase (H+-transporting)"
source_database: "KEGG"
source_id: "R11335"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11335"
---

# ubiquinol:oxygen oxidoreductase (H+-transporting)

`reaction.R11335`

## Static

- Type: `reaction`
- Source: `KEGG:R11335`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Ubiquinol + Oxygen + 8 H+ 2 Ubiquinone + 2 H2O + 8 H+

## Biological Role

Catalyzed by cyoB (protein.P0ABI8), cyoA (protein.P0ABJ1). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), Ubiquinol (molecule.C00390). Products: H2O (molecule.C00001), H+ (molecule.C00080), Ubiquinone (molecule.C00399).

## Annotation

2 Ubiquinol + Oxygen + 8 H+ <=> 2 Ubiquinone + 2 H2O + 8 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0ABI8|protein.P0ABI8]] `KEGG` `database` - via EC:7.1.1.3
- `catalyzes` <-- [[protein.P0ABJ1|protein.P0ABJ1]] `KEGG` `database` - via EC:7.1.1.3
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_product_of` <-- [[molecule.C00399|molecule.C00399]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080

## External IDs

- `KEGG:R11335`

## Notes

EQUATION: 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
