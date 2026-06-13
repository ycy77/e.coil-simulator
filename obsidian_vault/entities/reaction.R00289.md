---
entity_id: "reaction.R00289"
entity_type: "reaction"
name: "UTP:alpha-D-glucose-1-phosphate uridylyltransferase"
source_database: "KEGG"
source_id: "R00289"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00289"
---

# UTP:alpha-D-glucose-1-phosphate uridylyltransferase

`reaction.R00289`

## Static

- Type: `reaction`
- Source: `KEGG:R00289`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + D-Glucose 1-phosphate Diphosphate + UDP-glucose

## Biological Role

Catalyzed by galF (protein.P0AAB6), galU (protein.P0AEP3). Substrates: UTP (molecule.C00075), D-Glucose 1-phosphate (molecule.C00103). Products: Diphosphate (molecule.C00013), UDP-glucose (molecule.C00029).

## Annotation

UTP + D-Glucose 1-phosphate <=> Diphosphate + UDP-glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AAB6|protein.P0AAB6]] `KEGG` `database` - via EC:2.7.7.9
- `catalyzes` <-- [[protein.P0AEP3|protein.P0AEP3]] `KEGG` `database` - via EC:2.7.7.9
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029
- `is_product_of` <-- [[molecule.C00029|molecule.C00029]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029
- `is_substrate_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029

## External IDs

- `KEGG:R00289`

## Notes

EQUATION: C00075 + C00103 <=> C00013 + C00029
