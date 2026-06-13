---
entity_id: "reaction.R04438"
entity_type: "reaction"
name: "dTDP-4-amino-4,6-dideoxy-D-galactose:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R04438"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04438"
---

# dTDP-4-amino-4,6-dideoxy-D-galactose:2-oxoglutarate aminotransferase

`reaction.R04438`

## Static

- Type: `reaction`
- Source: `KEGG:R04438`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

dTDP-4-amino-4,6-dideoxy-D-galactose + 2-Oxoglutarate dTDP-4-oxo-6-deoxy-D-glucose + L-Glutamate

## Biological Role

Catalyzed by wecE (protein.P27833). Substrates: 2-Oxoglutarate (molecule.C00026), dTDP-4-amino-4,6-dideoxy-D-galactose (molecule.C04346). Products: L-Glutamate (molecule.C00025), dTDP-4-oxo-6-deoxy-D-glucose (molecule.C11907).

## Annotation

dTDP-4-amino-4,6-dideoxy-D-galactose + 2-Oxoglutarate <=> dTDP-4-oxo-6-deoxy-D-glucose + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27833|protein.P27833]] `KEGG` `database` - via EC:2.6.1.59
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_product_of` <-- [[molecule.C11907|molecule.C11907]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_substrate_of` <-- [[molecule.C04346|molecule.C04346]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025

## External IDs

- `KEGG:R04438`

## Notes

EQUATION: C04346 + C00026 <=> C11907 + C00025
