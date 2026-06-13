---
entity_id: "reaction.ecocyc.RXN-19338"
entity_type: "reaction"
name: "RXN-19338"
source_database: "EcoCyc"
source_id: "RXN-19338"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19338

`reaction.ecocyc.RXN-19338`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19338`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduced-Flavoproteins + CPD-20906 -> Oxidized-Flavoproteins + PROTON + CPD-20907; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Reduced-Flavoproteins + CPD-20906 -> Oxidized-Flavoproteins + PROTON + CPD-20907; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: [corrinoid adenosyltranferase]-cob(II)inamide (molecule.ecocyc.CPD-20906). Products: H+ (molecule.C00080), [corrinoid adenosyltranferase]-cob(I)inamide (molecule.ecocyc.CPD-20907).

## Enriched Pathways

- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Annotation

Reduced-Flavoproteins + CPD-20906 -> Oxidized-Flavoproteins + PROTON + CPD-20907; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20907|molecule.ecocyc.CPD-20907]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20906|molecule.ecocyc.CPD-20906]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19338`

## Notes

Reduced-Flavoproteins + CPD-20906 -> Oxidized-Flavoproteins + PROTON + CPD-20907; direction=PHYSIOL-LEFT-TO-RIGHT
