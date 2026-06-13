---
entity_id: "reaction.ecocyc.RXN-11135"
entity_type: "reaction"
name: "RXN-11135"
source_database: "EcoCyc"
source_id: "RXN-11135"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11135

`reaction.ecocyc.RXN-11135`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11135`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + WATER + Supercoiled-Duplex-DNAs -> ADP + Pi + PROTON + Single-Stranded-DNAs; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + WATER + Supercoiled-Duplex-DNAs -> ADP + Pi + PROTON + Single-Stranded-DNAs; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ATP-dependent DNA helicase Rep (complex.ecocyc.CPLX0-3931), DNA helicase II (complex.ecocyc.CPLX0-8111), recB (protein.P08394), helD (protein.P15038), recQ (protein.P15043), recG (protein.P24230). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + WATER + Supercoiled-Duplex-DNAs -> ADP + Pi + PROTON + Single-Stranded-DNAs; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3931|complex.ecocyc.CPLX0-3931]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8111|complex.ecocyc.CPLX0-8111]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P08394|protein.P08394]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P15038|protein.P15038]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P15043|protein.P15043]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P24230|protein.P24230]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11135`

## Notes

ATP + WATER + Supercoiled-Duplex-DNAs -> ADP + Pi + PROTON + Single-Stranded-DNAs; direction=PHYSIOL-LEFT-TO-RIGHT
