---
entity_id: "reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN"
entity_type: "reaction"
name: "GUANOSINE-DIPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "GUANOSINE-DIPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GUANOSINE-DIPHOSPHATASE-RXN

`reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GUANOSINE-DIPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GDP + WATER -> PROTON + GMP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GDP + WATER -> PROTON + GMP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudJ (protein.P0AEI6). Substrates: H2O (molecule.C00001), GDP (molecule.C00035). Products: H+ (molecule.C00080), GMP (molecule.C00144), phosphate (molecule.ecocyc.Pi).

## Annotation

GDP + WATER -> PROTON + GMP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEI6|protein.P0AEI6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GUANOSINE-DIPHOSPHATASE-RXN`

## Notes

GDP + WATER -> PROTON + GMP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
