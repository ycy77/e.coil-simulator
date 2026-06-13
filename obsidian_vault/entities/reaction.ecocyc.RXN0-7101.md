---
entity_id: "reaction.ecocyc.RXN0-7101"
entity_type: "reaction"
name: "RXN0-7101"
source_database: "EcoCyc"
source_id: "RXN0-7101"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7101

`reaction.ecocyc.RXN0-7101`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7101`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUCONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: GLUCONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by 5-keto-D-gluconate 5-reductase (complex.ecocyc.CPLX0-8292), kduD (protein.P37769). Substrates: NAD+ (molecule.C00003), D-Gluconic acid (molecule.C00257). Products: NADH (molecule.C00004), H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE).

## Annotation

GLUCONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8292|complex.ecocyc.CPLX0-8292]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37769|protein.P37769]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7101`

## Notes

GLUCONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=REVERSIBLE
