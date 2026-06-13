---
entity_id: "reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN"
entity_type: "reaction"
name: "ALTRO-OXIDOREDUCT-RXN"
source_database: "EcoCyc"
source_id: "ALTRO-OXIDOREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALTRO-OXIDOREDUCT-RXN

`reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALTRO-OXIDOREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the galacturonate pathway. EcoCyc reaction equation: NAD + D-ALTRONATE -> PROTON + NADH + D-TAGATURONATE; direction=REVERSIBLE. Part of the galacturonate pathway.

## Biological Role

Catalyzed by uxaB (protein.P0A6L7). Substrates: NAD+ (molecule.C00003), D-Altronate (molecule.C00817). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Tagaturonate (molecule.C00558).

## Enriched Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)

## Annotation

Part of the galacturonate pathway.

## Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A6L7|protein.P0A6L7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00558|molecule.C00558]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00817|molecule.C00817]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00514|molecule.C00514]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00905|molecule.C00905]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALTRO-OXIDOREDUCT-RXN`

## Notes

NAD + D-ALTRONATE -> PROTON + NADH + D-TAGATURONATE; direction=REVERSIBLE
