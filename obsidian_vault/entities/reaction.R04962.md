---
entity_id: "reaction.R04962"
entity_type: "reaction"
name: "decanoyl-[acp]:NADP+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04962"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04962"
---

# decanoyl-[acp]:NADP+ trans-2-oxidoreductase

`reaction.R04962`

## Static

- Type: `reaction`
- Source: `KEGG:R04962`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Decanoyl-[acp] + NADP+ trans-Dec-2-enoyl-[acp] + NADPH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NADP+ (molecule.C00006), Decanoyl-[acp] (molecule.C05755). Products: NADPH (molecule.C00005), H+ (molecule.C00080), trans-Dec-2-enoyl-[acp] (molecule.C05754).

## Annotation

Decanoyl-[acp] + NADP+ <=> trans-Dec-2-enoyl-[acp] + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.10
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080
- `is_product_of` <-- [[molecule.C05754|molecule.C05754]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C05755|molecule.C05755]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080

## External IDs

- `KEGG:R04962`

## Notes

EQUATION: C05755 + C00006 <=> C05754 + C00005 + C00080
