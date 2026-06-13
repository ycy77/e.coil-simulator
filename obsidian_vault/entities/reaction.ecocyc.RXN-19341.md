---
entity_id: "reaction.ecocyc.RXN-19341"
entity_type: "reaction"
name: "RXN-19341"
source_database: "EcoCyc"
source_id: "RXN-19341"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19341

`reaction.ecocyc.RXN-19341`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19341`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

COB-I-ALAMIN + Oxidized-Flavoproteins + PROTON -> CPD-1829 + Reduced-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: COB-I-ALAMIN + Oxidized-Flavoproteins + PROTON -> CPD-1829 + Reduced-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Cob(I)alamin (molecule.C00853). Products: Cob(II)alamin (molecule.C00541).

## Enriched Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Annotation

COB-I-ALAMIN + Oxidized-Flavoproteins + PROTON -> CPD-1829 + Reduced-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00541|molecule.C00541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19341`

## Notes

COB-I-ALAMIN + Oxidized-Flavoproteins + PROTON -> CPD-1829 + Reduced-Flavoproteins; direction=PHYSIOL-LEFT-TO-RIGHT
