---
entity_id: "reaction.R00567"
entity_type: "reaction"
name: "arginine racemase"
source_database: "KEGG"
source_id: "R00567"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00567"
---

# arginine racemase

`reaction.R00567`

## Static

- Type: `reaction`
- Source: `KEGG:R00567`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Arginine D-Arginine

## Biological Role

Catalyzed by ygeA (protein.P03813). Substrates: L-Arginine (molecule.C00062). Products: D-Arginine (molecule.C00792).

## Annotation

L-Arginine <=> D-Arginine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P03813|protein.P03813]] `KEGG` `database` - via EC:5.1.1.10
- `is_product_of` <-- [[molecule.C00792|molecule.C00792]] `KEGG` `database` - C00062 <=> C00792
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `KEGG` `database` - C00062 <=> C00792

## External IDs

- `KEGG:R00567`

## Notes

EQUATION: C00062 <=> C00792
