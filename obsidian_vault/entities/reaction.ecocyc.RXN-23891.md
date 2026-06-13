---
entity_id: "reaction.ecocyc.RXN-23891"
entity_type: "reaction"
name: "RXN-23891"
source_database: "EcoCyc"
source_id: "RXN-23891"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23891

`reaction.ecocyc.RXN-23891`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23891`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MET + ATP + PROTON -> CPD-26472 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MET + ATP + PROTON -> CPD-26472 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Methionine (molecule.C00073), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-methionyl)adenylate (molecule.ecocyc.CPD-26472).

## Annotation

MET + ATP + PROTON -> CPD-26472 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26472|molecule.ecocyc.CPD-26472]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23891`

## Notes

MET + ATP + PROTON -> CPD-26472 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
