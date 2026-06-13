---
entity_id: "reaction.R00405"
entity_type: "reaction"
name: "succinate:CoA ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R00405"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00405"
---

# succinate:CoA ligase (ADP-forming)

`reaction.R00405`

## Static

- Type: `reaction`
- Source: `KEGG:R00405`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Succinate + CoA ADP + Orthophosphate + Succinyl-CoA

## Biological Role

Catalyzed by sucC (protein.P0A836), sucD (protein.P0AGE9). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Succinate (molecule.C00042). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), Succinyl-CoA (molecule.C00091).

## Annotation

ATP + Succinate + CoA <=> ADP + Orthophosphate + Succinyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A836|protein.P0A836]] `KEGG` `database` - via EC:6.2.1.5
- `catalyzes` <-- [[protein.P0AGE9|protein.P0AGE9]] `KEGG` `database` - via EC:6.2.1.5
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_product_of` <-- [[molecule.C00091|molecule.C00091]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091

## External IDs

- `KEGG:R00405`

## Notes

EQUATION: C00002 + C00042 + C00010 <=> C00008 + C00009 + C00091
