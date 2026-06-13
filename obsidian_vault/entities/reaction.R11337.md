---
entity_id: "reaction.R11337"
entity_type: "reaction"
name: "(R)-2-hydroxyglutarate:NAD+ 2-oxidireductase"
source_database: "KEGG"
source_id: "R11337"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11337"
---

# (R)-2-hydroxyglutarate:NAD+ 2-oxidireductase

`reaction.R11337`

## Static

- Type: `reaction`
- Source: `KEGG:R11337`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-2-Hydroxyglutarate + NAD+ 2-Oxoglutarate + NADH + H+

## Biological Role

Catalyzed by serA (protein.P0A9T0). Substrates: NAD+ (molecule.C00003), (R)-2-Hydroxyglutarate (molecule.C01087). Products: NADH (molecule.C00004), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Annotation

(R)-2-Hydroxyglutarate + NAD+ <=> 2-Oxoglutarate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A9T0|protein.P0A9T0]] `KEGG` `database` - via EC:1.1.1.399
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C01087|molecule.C01087]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080

## External IDs

- `KEGG:R11337`

## Notes

EQUATION: C01087 + C00003 <=> C00026 + C00004 + C00080
