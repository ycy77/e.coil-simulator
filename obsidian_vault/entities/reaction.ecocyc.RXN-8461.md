---
entity_id: "reaction.ecocyc.RXN-8461"
entity_type: "reaction"
name: "RXN-8461"
source_database: "EcoCyc"
source_id: "RXN-8461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8461

`reaction.ecocyc.RXN-8461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8461`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-253 -> PROTON + CPD-8651 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-253 -> PROTON + CPD-8651 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: 4-(L-Alanin-3-yl)-2-hydroxy-cis,cis-muconate 6-semialdehyde (molecule.C04796). Products: H2O (molecule.C00001), H+ (molecule.C00080), betalamate (molecule.ecocyc.CPD-8651).

## Annotation

CPD-253 -> PROTON + CPD-8651 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8651|molecule.ecocyc.CPD-8651]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04796|molecule.C04796]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8461`

## Notes

CPD-253 -> PROTON + CPD-8651 + WATER; direction=LEFT-TO-RIGHT
