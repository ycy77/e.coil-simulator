---
entity_id: "reaction.R00792"
entity_type: "reaction"
name: "ferrocytochrome-b:nitrate oxidoreductase"
source_database: "KEGG"
source_id: "R00792"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00792"
---

# ferrocytochrome-b:nitrate oxidoreductase

`reaction.R00792`

## Static

- Type: `reaction`
- Source: `KEGG:R00792`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nitrate + 2 Ferrocytochrome b Nitrite + H2O + 2 Ferricytochrome b

## Biological Role

Catalyzed by napA (protein.P33937). Substrates: Nitrate (molecule.C00244). Products: H2O (molecule.C00001), Nitrite (molecule.C00088).

## Annotation

Nitrate + 2 Ferrocytochrome b <=> Nitrite + H2O + 2 Ferricytochrome b

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P33937|protein.P33937]] `KEGG` `database` - via EC:1.9.6.1
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00244 + 2 C06259 <=> C00088 + C00001 + 2 C06260
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `KEGG` `database` - C00244 + 2 C06259 <=> C00088 + C00001 + 2 C06260
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `KEGG` `database` - C00244 + 2 C06259 <=> C00088 + C00001 + 2 C06260

## External IDs

- `KEGG:R00792`

## Notes

EQUATION: C00244 + 2 C06259 <=> C00088 + C00001 + 2 C06260
