---
entity_id: "reaction.ecocyc.RXN-19334"
entity_type: "reaction"
name: "RXN-19334"
source_database: "EcoCyc"
source_id: "RXN-19334"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19334

`reaction.ecocyc.RXN-19334`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19334`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-20904 + Reduced-Flavoproteins -> CPD-20905 + Oxidized-Flavoproteins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20904 + Reduced-Flavoproteins -> CPD-20905 + Oxidized-Flavoproteins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: cob(II)alamin-[corrinoid adenosyltranferase] (molecule.ecocyc.CPD-20904). Products: H+ (molecule.C00080), cob(I)alamin-[corrinoid adenosyltranferase] (molecule.ecocyc.CPD-20905).

## Enriched Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Annotation

CPD-20904 + Reduced-Flavoproteins -> CPD-20905 + Oxidized-Flavoproteins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20905|molecule.ecocyc.CPD-20905]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20904|molecule.ecocyc.CPD-20904]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19334`

## Notes

CPD-20904 + Reduced-Flavoproteins -> CPD-20905 + Oxidized-Flavoproteins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
