---
entity_id: "reaction.ecocyc.RXN-16281"
entity_type: "reaction"
name: "RXN-16281"
source_database: "EcoCyc"
source_id: "RXN-16281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16281

`reaction.ecocyc.RXN-16281`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16281`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

KDO2-LIPID-A + UNDECAPRENYL-DIPHOSPHATE -> CPD-17530 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: KDO2-LIPID-A + UNDECAPRENYL-DIPHOSPHATE -> CPD-17530 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxT (protein.P76445). Substrates: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), KDO2-lipid A (molecule.C06026). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), α-D-Kdo-(2→4)-α-D-Kdo-(2→6)-lipid A 1-diphosphate (molecule.ecocyc.CPD-17530).

## Annotation

KDO2-LIPID-A + UNDECAPRENYL-DIPHOSPHATE -> CPD-17530 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76445|protein.P76445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17530|molecule.ecocyc.CPD-17530]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16281`

## Notes

KDO2-LIPID-A + UNDECAPRENYL-DIPHOSPHATE -> CPD-17530 + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT
