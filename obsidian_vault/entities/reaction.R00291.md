---
entity_id: "reaction.R00291"
entity_type: "reaction"
name: "UDP-glucose 4-epimerase;"
source_database: "KEGG"
source_id: "R00291"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00291"
---

# UDP-glucose 4-epimerase;

`reaction.R00291`

## Static

- Type: `reaction`
- Source: `KEGG:R00291`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-glucose UDP-alpha-D-galactose

## Biological Role

Catalyzed by galE (protein.P09147). Substrates: UDP-glucose (molecule.C00029). Products: UDP-alpha-D-galactose (molecule.C00052).

## Annotation

UDP-glucose <=> UDP-alpha-D-galactose

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P09147|protein.P09147]] `KEGG` `database` - via EC:5.1.3.2
- `is_product_of` <-- [[molecule.C00052|molecule.C00052]] `KEGG` `database` - C00029 <=> C00052
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `KEGG` `database` - C00029 <=> C00052

## External IDs

- `KEGG:R00291`

## Notes

EQUATION: C00029 <=> C00052
