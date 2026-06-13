---
entity_id: "reaction.R00348"
entity_type: "reaction"
name: "2-oxosuccinamate amidohydrolase"
source_database: "KEGG"
source_id: "R00348"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00348"
---

# 2-oxosuccinamate amidohydrolase

`reaction.R00348`

## Static

- Type: `reaction`
- Source: `KEGG:R00348`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxosuccinamate + H2O Oxaloacetate + Ammonia

## Biological Role

Catalyzed by yafV (protein.Q47679). Substrates: H2O (molecule.C00001), 2-Oxosuccinamate (molecule.C02362). Products: Ammonia (molecule.C00014), Oxaloacetate (molecule.C00036).

## Annotation

2-Oxosuccinamate + H2O <=> Oxaloacetate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q47679|protein.Q47679]] `KEGG` `database` - via EC:3.5.1.3
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C02362 + C00001 <=> C00036 + C00014
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C02362 + C00001 <=> C00036 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02362 + C00001 <=> C00036 + C00014
- `is_substrate_of` <-- [[molecule.C02362|molecule.C02362]] `KEGG` `database` - C02362 + C00001 <=> C00036 + C00014

## External IDs

- `KEGG:R00348`

## Notes

EQUATION: C02362 + C00001 <=> C00036 + C00014
