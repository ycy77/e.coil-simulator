---
entity_id: "reaction.R09796"
entity_type: "reaction"
name: "(R)-lactate hydro-lyase"
source_database: "KEGG"
source_id: "R09796"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09796"
---

# (R)-lactate hydro-lyase

`reaction.R09796`

## Static

- Type: `reaction`
- Source: `KEGG:R09796`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-Lactate Methylglyoxal + H2O

## Biological Role

Catalyzed by hchA (protein.P31658). Substrates: (R)-Lactate (molecule.C00256). Products: H2O (molecule.C00001), Methylglyoxal (molecule.C00546).

## Annotation

(R)-Lactate <=> Methylglyoxal + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P31658|protein.P31658]] `KEGG` `database` - via EC:4.2.1.130
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00256 <=> C00546 + C00001
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `KEGG` `database` - C00256 <=> C00546 + C00001
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `KEGG` `database` - C00256 <=> C00546 + C00001

## External IDs

- `KEGG:R09796`

## Notes

EQUATION: C00256 <=> C00546 + C00001
