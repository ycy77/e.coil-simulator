---
entity_id: "reaction.R00078"
entity_type: "reaction"
name: "Fe(II):oxygen oxidoreductase;"
source_database: "KEGG"
source_id: "R00078"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00078"
---

# Fe(II):oxygen oxidoreductase;

`reaction.R00078`

## Static

- Type: `reaction`
- Source: `KEGG:R00078`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxygen + 4 Fe2+ + 4 H+ 4 Fe3+ + 2 H2O

## Biological Role

Catalyzed by bfr (protein.P0ABD3). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), Fe2+ (molecule.C14818). Products: H2O (molecule.C00001), Fe3+ (molecule.C14819).

## Annotation

Oxygen + 4 Fe2+ + 4 H+ <=> 4 Fe3+ + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABD3|protein.P0ABD3]] `KEGG` `database` - via EC:1.16.3.1
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
- `is_product_of` <-- [[molecule.C14819|molecule.C14819]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `KEGG` `database` - C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001

## External IDs

- `KEGG:R00078`

## Notes

EQUATION: C00007 + 4 C14818 + 4 C00080 <=> 4 C14819 + 2 C00001
