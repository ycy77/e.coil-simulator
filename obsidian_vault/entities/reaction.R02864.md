---
entity_id: "reaction.R02864"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:uroporphyrin-III C-methyltransferase"
source_database: "KEGG"
source_id: "R02864"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02864"
---

# S-adenosyl-L-methionine:uroporphyrin-III C-methyltransferase

`reaction.R02864`

## Static

- Type: `reaction`
- Source: `KEGG:R02864`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Siroheme + 2 H+ Fe2+ + Sirohydrochlorin

## Biological Role

Catalyzed by cysG (protein.P0AEA8). Substrates: H+ (molecule.C00080), Siroheme (molecule.C00748). Products: Sirohydrochlorin (molecule.C05778), Fe2+ (molecule.C14818).

## Annotation

Siroheme + 2 H+ <=> Fe2+ + Sirohydrochlorin

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEA8|protein.P0AEA8]] `KEGG` `database` - via EC:4.99.1.4
- `is_product_of` <-- [[molecule.C05778|molecule.C05778]] `KEGG` `database` - C00748 + 2 C00080 <=> C14818 + C05778
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `KEGG` `database` - C00748 + 2 C00080 <=> C14818 + C05778
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00748 + 2 C00080 <=> C14818 + C05778
- `is_substrate_of` <-- [[molecule.C00748|molecule.C00748]] `KEGG` `database` - C00748 + 2 C00080 <=> C14818 + C05778

## External IDs

- `KEGG:R02864`

## Notes

EQUATION: C00748 + 2 C00080 <=> C14818 + C05778
