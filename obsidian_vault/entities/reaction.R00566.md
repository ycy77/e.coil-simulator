---
entity_id: "reaction.R00566"
entity_type: "reaction"
name: "L-arginine carboxy-lyase (agmatine-forming)"
source_database: "KEGG"
source_id: "R00566"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00566"
---

# L-arginine carboxy-lyase (agmatine-forming)

`reaction.R00566`

## Static

- Type: `reaction`
- Source: `KEGG:R00566`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Arginine Agmatine + CO2

## Biological Role

Catalyzed by speA (protein.P21170), adiA (protein.P28629). Substrates: L-Arginine (molecule.C00062). Products: CO2 (molecule.C00011), Agmatine (molecule.C00179).

## Annotation

L-Arginine <=> Agmatine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21170|protein.P21170]] `KEGG` `database` - via EC:4.1.1.19
- `catalyzes` <-- [[protein.P28629|protein.P28629]] `KEGG` `database` - via EC:4.1.1.19
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00062 <=> C00179 + C00011
- `is_product_of` <-- [[molecule.C00179|molecule.C00179]] `KEGG` `database` - C00062 <=> C00179 + C00011
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `KEGG` `database` - C00062 <=> C00179 + C00011

## External IDs

- `KEGG:R00566`

## Notes

EQUATION: C00062 <=> C00179 + C00011
