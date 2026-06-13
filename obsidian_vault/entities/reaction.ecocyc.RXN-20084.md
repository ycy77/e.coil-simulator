---
entity_id: "reaction.ecocyc.RXN-20084"
entity_type: "reaction"
name: "RXN-20084"
source_database: "EcoCyc"
source_id: "RXN-20084"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20084

`reaction.ecocyc.RXN-20084`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20084`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLT + NADP + WATER -> AMMONIA + 2-KETOGLUTARATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: GLT + NADP + WATER -> AMMONIA + 2-KETOGLUTARATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), L-Glutamate (molecule.C00025). Products: NADPH (molecule.C00005), Ammonia (molecule.C00014), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.AMMASSIM-PWY` ammonia assimilation cycle III (EcoCyc)
- `ecocyc.GLUTSYN-PWY` L-glutamate biosynthesis I (EcoCyc)

## Annotation

GLT + NADP + WATER -> AMMONIA + 2-KETOGLUTARATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.AMMASSIM-PWY` ammonia assimilation cycle III (EcoCyc)
- `ecocyc.GLUTSYN-PWY` L-glutamate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20084`

## Notes

GLT + NADP + WATER -> AMMONIA + 2-KETOGLUTARATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
