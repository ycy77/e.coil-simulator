---
entity_id: "reaction.R00355"
entity_type: "reaction"
name: "L-aspartate:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R00355"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00355"
---

# L-aspartate:2-oxoglutarate aminotransferase

`reaction.R00355`

## Static

- Type: `reaction`
- Source: `KEGG:R00355`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Aspartate + 2-Oxoglutarate Oxaloacetate + L-Glutamate

## Biological Role

Catalyzed by aspC (protein.P00509). Substrates: 2-Oxoglutarate (molecule.C00026), L-Aspartate (molecule.C00049). Products: L-Glutamate (molecule.C00025), Oxaloacetate (molecule.C00036).

## Annotation

L-Aspartate + 2-Oxoglutarate <=> Oxaloacetate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00509|protein.P00509]] `KEGG` `database` - via EC:2.6.1.1
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025

## External IDs

- `KEGG:R00355`

## Notes

EQUATION: C00049 + C00026 <=> C00036 + C00025
