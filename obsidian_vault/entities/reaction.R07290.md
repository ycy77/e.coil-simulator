---
entity_id: "reaction.R07290"
entity_type: "reaction"
name: "formyl-CoA:oxalate CoA-transferase"
source_database: "KEGG"
source_id: "R07290"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07290"
---

# formyl-CoA:oxalate CoA-transferase

`reaction.R07290`

## Static

- Type: `reaction`
- Source: `KEGG:R07290`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Formyl-CoA + Oxalate Formate + Oxalyl-CoA

## Biological Role

Catalyzed by frc (protein.P69902). Substrates: Oxalate (molecule.C00209), Formyl-CoA (molecule.C00798). Products: Formate (molecule.C00058), Oxalyl-CoA (molecule.C00313).

## Annotation

Formyl-CoA + Oxalate <=> Formate + Oxalyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P69902|protein.P69902]] `KEGG` `database` - via EC:2.8.3.16
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313
- `is_product_of` <-- [[molecule.C00313|molecule.C00313]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313
- `is_substrate_of` <-- [[molecule.C00209|molecule.C00209]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313
- `is_substrate_of` <-- [[molecule.C00798|molecule.C00798]] `KEGG` `database` - C00798 + C00209 <=> C00058 + C00313

## External IDs

- `KEGG:R07290`

## Notes

EQUATION: C00798 + C00209 <=> C00058 + C00313
