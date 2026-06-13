---
entity_id: "reaction.R04964"
entity_type: "reaction"
name: "(3R)-3-hydroxydodecanoyl-[acyl-carrier-protein]:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R04964"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04964"
---

# (3R)-3-hydroxydodecanoyl-[acyl-carrier-protein]:NADP+ oxidoreductase

`reaction.R04964`

## Static

- Type: `reaction`
- Source: `KEGG:R04964`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(3R)-3-Hydroxydodecanoyl-[acyl-carrier protein] + NADP+ 3-Oxododecanoyl-[acp] + NADPH + H+

## Biological Role

Catalyzed by fabG (protein.P0AEK2). Substrates: NADP+ (molecule.C00006), (3R)-3-Hydroxydodecanoyl-[acyl-carrier protein] (molecule.C05757). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Oxododecanoyl-[acp] (molecule.C05756).

## Annotation

(3R)-3-Hydroxydodecanoyl-[acyl-carrier protein] + NADP+ <=> 3-Oxododecanoyl-[acp] + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK2|protein.P0AEK2]] `KEGG` `database` - via EC:1.1.1.100
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080
- `is_product_of` <-- [[molecule.C05756|molecule.C05756]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C05757|molecule.C05757]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080

## External IDs

- `KEGG:R04964`

## Notes

EQUATION: C05757 + C00006 <=> C05756 + C00005 + C00080
