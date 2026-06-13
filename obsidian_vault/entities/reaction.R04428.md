---
entity_id: "reaction.R04428"
entity_type: "reaction"
name: "(3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydro-lyase"
source_database: "KEGG"
source_id: "R04428"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04428"
---

# (3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydro-lyase

`reaction.R04428`

## Static

- Type: `reaction`
- Source: `KEGG:R04428`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(3R)-3-Hydroxybutanoyl-[acyl-carrier protein] But-2-enoyl-[acyl-carrier protein] + H2O

## Biological Role

Catalyzed by fabA (protein.P0A6Q3), fabZ (protein.P0A6Q6). Substrates: (3R)-3-Hydroxybutanoyl-[acyl-carrier protein] (molecule.C04618). Products: H2O (molecule.C00001), But-2-enoyl-[acyl-carrier protein] (molecule.C04246).

## Annotation

(3R)-3-Hydroxybutanoyl-[acyl-carrier protein] <=> But-2-enoyl-[acyl-carrier protein] + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6Q3|protein.P0A6Q3]] `KEGG` `database` - via EC:4.2.1.59
- `catalyzes` <-- [[protein.P0A6Q6|protein.P0A6Q6]] `KEGG` `database` - via EC:4.2.1.59
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04618 <=> C04246 + C00001
- `is_product_of` <-- [[molecule.C04246|molecule.C04246]] `KEGG` `database` - C04618 <=> C04246 + C00001
- `is_substrate_of` <-- [[molecule.C04618|molecule.C04618]] `KEGG` `database` - C04618 <=> C04246 + C00001

## External IDs

- `KEGG:R04428`

## Notes

EQUATION: C04618 <=> C04246 + C00001
