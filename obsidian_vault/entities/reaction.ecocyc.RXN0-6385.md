---
entity_id: "reaction.ecocyc.RXN0-6385"
entity_type: "reaction"
name: "RXN0-6385"
source_database: "EcoCyc"
source_id: "RXN0-6385"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6385

`reaction.ecocyc.RXN0-6385`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6385`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Red-Thioredoxin + S2O3 -> Ox-Thioredoxin + SO3 + HS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Red-Thioredoxin + S2O3 -> Ox-Thioredoxin + SO3 + HS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thiosulfate sulfurtransferase GlpE (complex.ecocyc.CPLX0-242). Substrates: Thiosulfate (molecule.C00320). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), Hydrogen sulfide (molecule.C00283).

## Annotation

Red-Thioredoxin + S2O3 -> Ox-Thioredoxin + SO3 + HS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-242|complex.ecocyc.CPLX0-242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6385`

## Notes

Red-Thioredoxin + S2O3 -> Ox-Thioredoxin + SO3 + HS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
