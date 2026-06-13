---
entity_id: "reaction.ecocyc.RXN0-6722"
entity_type: "reaction"
name: "RXN0-6722"
source_database: "EcoCyc"
source_id: "RXN0-6722"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6722

`reaction.ecocyc.RXN0-6722`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6722`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Quinones + NADH + PROTON -> NAD + Semiquinones; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Quinones + NADH + PROTON -> NAD + Semiquinones; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by FMN dependent NADH:quinone oxidoreductase (complex.ecocyc.CPLX0-7693). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), a quinone (molecule.ecocyc.Quinones). Products: NAD+ (molecule.C00003), a semiquinone (molecule.ecocyc.Semiquinones).

## Annotation

Quinones + NADH + PROTON -> NAD + Semiquinones; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7693|complex.ecocyc.CPLX0-7693]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Semiquinones|molecule.ecocyc.Semiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Quinones|molecule.ecocyc.Quinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6722`

## Notes

Quinones + NADH + PROTON -> NAD + Semiquinones; direction=PHYSIOL-LEFT-TO-RIGHT
