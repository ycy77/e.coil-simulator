---
entity_id: "reaction.ecocyc.RXN-9550"
entity_type: "reaction"
name: "RXN-9550"
source_database: "EcoCyc"
source_id: "RXN-9550"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9550

`reaction.ecocyc.RXN-9550`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9550`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Palmitoleoyl-ACPs + WATER -> CPD-9245 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Palmitoleoyl-ACPs + WATER -> CPD-9245 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1 (complex.ecocyc.CPLX0-7630). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), (9Z)-Hexadecenoic acid (molecule.C08362).

## Enriched Pathways

- `ecocyc.PWY-6282` palmitoleate biosynthesis I (from (5Z)-dodec-5-enoate) (EcoCyc)

## Annotation

Palmitoleoyl-ACPs + WATER -> CPD-9245 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6282` palmitoleate biosynthesis I (from (5Z)-dodec-5-enoate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7630|complex.ecocyc.CPLX0-7630]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C08362|molecule.C08362]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9550`

## Notes

Palmitoleoyl-ACPs + WATER -> CPD-9245 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
