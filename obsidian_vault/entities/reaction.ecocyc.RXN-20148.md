---
entity_id: "reaction.ecocyc.RXN-20148"
entity_type: "reaction"
name: "RXN-20148"
source_database: "EcoCyc"
source_id: "RXN-20148"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20148

`reaction.ecocyc.RXN-20148`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20148`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

OXYGEN-MOLECULE + Ubiquinols -> SUPER-OXIDE + Ubiquinones + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: OXYGEN-MOLECULE + Ubiquinols -> SUPER-OXIDE + Ubiquinones + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by cybB (protein.P0ABE5). Substrates: Oxygen (molecule.C00007), Ubiquinol (molecule.C00390). Products: H+ (molecule.C00080), superoxide (molecule.ecocyc.SUPER-OXIDE), a ubiquinone (molecule.ecocyc.Ubiquinones).

## Annotation

OXYGEN-MOLECULE + Ubiquinols -> SUPER-OXIDE + Ubiquinones + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABE5|protein.P0ABE5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20148`

## Notes

OXYGEN-MOLECULE + Ubiquinols -> SUPER-OXIDE + Ubiquinones + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
