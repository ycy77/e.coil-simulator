---
entity_id: "reaction.R00217"
entity_type: "reaction"
name: "oxaloacetate carboxy-lyase (pyruvate-forming)"
source_database: "KEGG"
source_id: "R00217"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00217"
---

# oxaloacetate carboxy-lyase (pyruvate-forming)

`reaction.R00217`

## Static

- Type: `reaction`
- Source: `KEGG:R00217`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxaloacetate Pyruvate + CO2

## Biological Role

Catalyzed by maeA (protein.P26616), maeB (protein.P76558). Substrates: Oxaloacetate (molecule.C00036). Products: CO2 (molecule.C00011), Pyruvate (molecule.C00022).

## Annotation

Oxaloacetate <=> Pyruvate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P26616|protein.P26616]] `KEGG` `database` - via EC:1.1.1.38
- `catalyzes` <-- [[protein.P76558|protein.P76558]] `KEGG` `database` - via EC:1.1.1.40
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00036 <=> C00022 + C00011
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00036 <=> C00022 + C00011
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00036 <=> C00022 + C00011

## External IDs

- `KEGG:R00217`

## Notes

EQUATION: C00036 <=> C00022 + C00011
