---
entity_id: "reaction.R03165"
entity_type: "reaction"
name: "hydroxymethylbilane hydro-lyase(cyclizing)"
source_database: "KEGG"
source_id: "R03165"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03165"
---

# hydroxymethylbilane hydro-lyase(cyclizing)

`reaction.R03165`

## Static

- Type: `reaction`
- Source: `KEGG:R03165`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxymethylbilane Uroporphyrinogen III + H2O

## Biological Role

Catalyzed by hemD (protein.P09126). Substrates: Hydroxymethylbilane (molecule.C01024). Products: H2O (molecule.C00001), Uroporphyrinogen III (molecule.C01051).

## Annotation

Hydroxymethylbilane <=> Uroporphyrinogen III + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P09126|protein.P09126]] `KEGG` `database` - via EC:4.2.1.75
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01024 <=> C01051 + C00001
- `is_product_of` <-- [[molecule.C01051|molecule.C01051]] `KEGG` `database` - C01024 <=> C01051 + C00001
- `is_substrate_of` <-- [[molecule.C01024|molecule.C01024]] `KEGG` `database` - C01024 <=> C01051 + C00001

## External IDs

- `KEGG:R03165`

## Notes

EQUATION: C01024 <=> C01051 + C00001
