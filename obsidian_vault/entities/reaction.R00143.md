---
entity_id: "reaction.R00143"
entity_type: "reaction"
name: "ammonia:NAD+ oxidoreductase;"
source_database: "KEGG"
source_id: "R00143"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00143"
---

# ammonia:NAD+ oxidoreductase;

`reaction.R00143`

## Static

- Type: `reaction`
- Source: `KEGG:R00143`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ammonia + NAD+ + H2O Hydroxylamine + NADH + H+

## Biological Role

Catalyzed by hcp (protein.P75825). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Ammonia (molecule.C00014). Products: NADH (molecule.C00004), H+ (molecule.C00080), Hydroxylamine (molecule.C00192).

## Annotation

Ammonia + NAD+ + H2O <=> Hydroxylamine + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P75825|protein.P75825]] `KEGG` `database` - via EC:1.7.99.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00192|molecule.C00192]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080

## External IDs

- `KEGG:R00143`

## Notes

EQUATION: C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
