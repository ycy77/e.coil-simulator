---
entity_id: "reaction.R02404"
entity_type: "reaction"
name: "itaconate:CoA ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R02404"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02404"
---

# itaconate:CoA ligase (ADP-forming)

`reaction.R02404`

## Static

- Type: `reaction`
- Source: `KEGG:R02404`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Itaconate + CoA ADP + Orthophosphate + Itaconyl-CoA

## Biological Role

Catalyzed by sucC (protein.P0A836), sucD (protein.P0AGE9). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Itaconate (molecule.C00490). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), Itaconyl-CoA (molecule.C00531).

## Annotation

ATP + Itaconate + CoA <=> ADP + Orthophosphate + Itaconyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A836|protein.P0A836]] `KEGG` `database` - via EC:6.2.1.5
- `catalyzes` <-- [[protein.P0AGE9|protein.P0AGE9]] `KEGG` `database` - via EC:6.2.1.5
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `is_product_of` <-- [[molecule.C00531|molecule.C00531]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
- `is_substrate_of` <-- [[molecule.C00490|molecule.C00490]] `KEGG` `database` - C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531

## External IDs

- `KEGG:R02404`

## Notes

EQUATION: C00002 + C00490 + C00010 <=> C00008 + C00009 + C00531
