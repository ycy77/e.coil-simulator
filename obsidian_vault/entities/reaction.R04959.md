---
entity_id: "reaction.R04959"
entity_type: "reaction"
name: "octanoyl-[acp]:NADP+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04959"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04959"
---

# octanoyl-[acp]:NADP+ trans-2-oxidoreductase

`reaction.R04959`

## Static

- Type: `reaction`
- Source: `KEGG:R04959`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Octanoyl-[acp] + NADP+ trans-Oct-2-enoyl-[acp] + NADPH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NADP+ (molecule.C00006), Octanoyl-[acp] (molecule.C05752). Products: NADPH (molecule.C00005), H+ (molecule.C00080), trans-Oct-2-enoyl-[acp] (molecule.C05751).

## Annotation

Octanoyl-[acp] + NADP+ <=> trans-Oct-2-enoyl-[acp] + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.10
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080
- `is_product_of` <-- [[molecule.C05751|molecule.C05751]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C05752|molecule.C05752]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080

## External IDs

- `KEGG:R04959`

## Notes

EQUATION: C05752 + C00006 <=> C05751 + C00005 + C00080
