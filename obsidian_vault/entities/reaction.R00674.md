---
entity_id: "reaction.R00674"
entity_type: "reaction"
name: "L-serine hydro-lyase (adding indole; L-tryptophan-forming)"
source_database: "KEGG"
source_id: "R00674"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00674"
---

# L-serine hydro-lyase (adding indole; L-tryptophan-forming)

`reaction.R00674`

## Static

- Type: `reaction`
- Source: `KEGG:R00674`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Serine + Indole L-Tryptophan + H2O

## Biological Role

Catalyzed by trpA (protein.P0A877), trpB (protein.P0A879). Substrates: L-Serine (molecule.C00065), Indole (molecule.C00463). Products: H2O (molecule.C00001), L-Tryptophan (molecule.C00078).

## Annotation

L-Serine + Indole <=> L-Tryptophan + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A877|protein.P0A877]] `KEGG` `database` - via EC:4.2.1.20
- `catalyzes` <-- [[protein.P0A879|protein.P0A879]] `KEGG` `database` - via EC:4.2.1.20
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001
- `is_product_of` <-- [[molecule.C00078|molecule.C00078]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001
- `is_substrate_of` <-- [[molecule.C00463|molecule.C00463]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001

## External IDs

- `KEGG:R00674`

## Notes

EQUATION: C00065 + C00463 <=> C00078 + C00001
