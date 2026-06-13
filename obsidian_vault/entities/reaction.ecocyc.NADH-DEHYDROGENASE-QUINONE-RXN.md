---
entity_id: "reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN"
entity_type: "reaction"
name: "NADH dehydrogenase (quinone)"
source_database: "EcoCyc"
source_id: "NADH-DEHYDROGENASE-QUINONE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NADH dehydrogenase (quinone)

`reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NADH-DEHYDROGENASE-QUINONE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-3766 + NADH + PROTON -> MENADIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3766 + NADH + PROTON -> MENADIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADH dehydrogenase (quinone) (complex.ecocyc.NQOR-CPLX). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), menadione (molecule.ecocyc.CPD-3766). Products: NAD+ (molecule.C00003), menadiol (molecule.ecocyc.MENADIOL).

## Annotation

CPD-3766 + NADH + PROTON -> MENADIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.NQOR-CPLX|complex.ecocyc.NQOR-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MENADIOL|molecule.ecocyc.MENADIOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3766|molecule.ecocyc.CPD-3766]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DICOUMAROL|molecule.ecocyc.DICOUMAROL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NADH-DEHYDROGENASE-QUINONE-RXN`

## Notes

CPD-3766 + NADH + PROTON -> MENADIOL + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
