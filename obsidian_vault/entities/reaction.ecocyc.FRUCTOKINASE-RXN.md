---
entity_id: "reaction.ecocyc.FRUCTOKINASE-RXN"
entity_type: "reaction"
name: "FRUCTOKINASE-RXN"
source_database: "EcoCyc"
source_id: "FRUCTOKINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "D-fructokinase"
---

# FRUCTOKINASE-RXN

`reaction.ecocyc.FRUCTOKINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FRUCTOKINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BETA-D-FRUCTOSE + ATP -> PROTON + FRUCTOSE-6P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: BETA-D-FRUCTOSE + ATP -> PROTON + FRUCTOSE-6P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mak (protein.P23917). Substrates: ATP (molecule.C00002), β-D-fructofuranose (molecule.ecocyc.BETA-D-FRUCTOSE). Products: ADP (molecule.C00008), H+ (molecule.C00080), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Annotation

BETA-D-FRUCTOSE + ATP -> PROTON + FRUCTOSE-6P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23917|protein.P23917]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.BETA-D-FRUCTOSE|molecule.ecocyc.BETA-D-FRUCTOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.D-Mannosamines|molecule.ecocyc.D-Mannosamines]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FRUCTOKINASE-RXN`

## Notes

BETA-D-FRUCTOSE + ATP -> PROTON + FRUCTOSE-6P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
