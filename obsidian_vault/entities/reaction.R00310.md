---
entity_id: "reaction.R00310"
entity_type: "reaction"
name: "protoheme ferro-lyase (protoporphyrin-forming)"
source_database: "KEGG"
source_id: "R00310"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00310"
---

# protoheme ferro-lyase (protoporphyrin-forming)

`reaction.R00310`

## Static

- Type: `reaction`
- Source: `KEGG:R00310`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protoporphyrin + Fe2+ Heme + 2 H+

## Biological Role

Catalyzed by hemH (protein.P23871). Substrates: Protoporphyrin (molecule.C02191), Fe2+ (molecule.C14818). Products: Heme (molecule.C00032), H+ (molecule.C00080).

## Annotation

Protoporphyrin + Fe2+ <=> Heme + 2 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P23871|protein.P23871]] `KEGG` `database` - via EC:4.98.1.1
- `is_product_of` <-- [[molecule.C00032|molecule.C00032]] `KEGG` `database` - C02191 + C14818 <=> C00032 + 2 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C02191 + C14818 <=> C00032 + 2 C00080
- `is_substrate_of` <-- [[molecule.C02191|molecule.C02191]] `KEGG` `database` - C02191 + C14818 <=> C00032 + 2 C00080
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `KEGG` `database` - C02191 + C14818 <=> C00032 + 2 C00080

## External IDs

- `KEGG:R00310`

## Notes

EQUATION: C02191 + C14818 <=> C00032 + 2 C00080
