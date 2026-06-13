---
entity_id: "reaction.ecocyc.RXN-25425"
entity_type: "reaction"
name: "RXN-25425"
source_database: "EcoCyc"
source_id: "RXN-25425"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25425

`reaction.ecocyc.RXN-25425`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25425`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12763 -> CPD-11764 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12763 -> CPD-11764 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 5-Aminopentanal (molecule.C12455). Products: H2O (molecule.C00001), H+ (molecule.C00080), 1-piperideine (molecule.ecocyc.CPD-11764).

## Annotation

CPD-12763 -> CPD-11764 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-11764|molecule.ecocyc.CPD-11764]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C12455|molecule.C12455]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25425`

## Notes

CPD-12763 -> CPD-11764 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
