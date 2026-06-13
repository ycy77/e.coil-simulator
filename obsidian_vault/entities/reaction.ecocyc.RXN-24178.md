---
entity_id: "reaction.ecocyc.RXN-24178"
entity_type: "reaction"
name: "RXN-24178"
source_database: "EcoCyc"
source_id: "RXN-24178"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24178

`reaction.ecocyc.RXN-24178`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24178`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ATP-dependent RNA helicase RhlB (complex.ecocyc.CPLX0-3541), ATP-dependent RNA helicase DeaD (complex.ecocyc.CPLX0-8557), srmB (protein.P21507), rhlE (protein.P25888). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3541|complex.ecocyc.CPLX0-3541]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8557|complex.ecocyc.CPLX0-8557]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21507|protein.P21507]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P25888|protein.P25888]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24178`

## Notes

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
