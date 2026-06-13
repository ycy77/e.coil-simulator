---
entity_id: "reaction.ecocyc.MANNKIN-RXN"
entity_type: "reaction"
name: "MANNKIN-RXN"
source_database: "EcoCyc"
source_id: "MANNKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MANNKIN-RXN

`reaction.ecocyc.MANNKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of mannose catabolism. EcoCyc reaction equation: D-mannopyranose + ATP -> CPD-15979 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. Part of mannose catabolism.

## Biological Role

Catalyzed by mak (protein.P23917). Substrates: ATP (molecule.C00002), D-mannopyranose (molecule.ecocyc.D-mannopyranose). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979).

## Annotation

Part of mannose catabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23917|protein.P23917]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-mannopyranose|molecule.ecocyc.D-mannopyranose]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.D-Mannosamines|molecule.ecocyc.D-Mannosamines]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MANNKIN-RXN`

## Notes

D-mannopyranose + ATP -> CPD-15979 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
