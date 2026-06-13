---
entity_id: "reaction.R01908"
entity_type: "reaction"
name: "oxalyl-CoA carboxy-lyase (formyl-CoA-forming)"
source_database: "KEGG"
source_id: "R01908"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01908"
---

# oxalyl-CoA carboxy-lyase (formyl-CoA-forming)

`reaction.R01908`

## Static

- Type: `reaction`
- Source: `KEGG:R01908`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxalyl-CoA Formyl-CoA + CO2

## Biological Role

Catalyzed by oxc (protein.P0AFI0). Substrates: Oxalyl-CoA (molecule.C00313). Products: CO2 (molecule.C00011), Formyl-CoA (molecule.C00798).

## Annotation

Oxalyl-CoA <=> Formyl-CoA + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AFI0|protein.P0AFI0]] `KEGG` `database` - via EC:4.1.1.8
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00313 <=> C00798 + C00011
- `is_product_of` <-- [[molecule.C00798|molecule.C00798]] `KEGG` `database` - C00313 <=> C00798 + C00011
- `is_substrate_of` <-- [[molecule.C00313|molecule.C00313]] `KEGG` `database` - C00313 <=> C00798 + C00011

## External IDs

- `KEGG:R01908`

## Notes

EQUATION: C00313 <=> C00798 + C00011
