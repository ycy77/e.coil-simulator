---
entity_id: "reaction.ecocyc.RXN-13072"
entity_type: "reaction"
name: "RXN-13072"
source_database: "EcoCyc"
source_id: "RXN-13072"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13072

`reaction.ecocyc.RXN-13072`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13072`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-KETO-GLUTARAMATE + WATER -> 2-KETOGLUTARATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-KETO-GLUTARAMATE + WATER -> 2-KETOGLUTARATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yafV (protein.Q47679). Substrates: H2O (molecule.C00001), 2-Oxoglutaramate (molecule.C00940). Products: 2-Oxoglutarate (molecule.C00026), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

2-KETO-GLUTARAMATE + WATER -> 2-KETOGLUTARATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q47679|protein.Q47679]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00940|molecule.C00940]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13072`

## Notes

2-KETO-GLUTARAMATE + WATER -> 2-KETOGLUTARATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
