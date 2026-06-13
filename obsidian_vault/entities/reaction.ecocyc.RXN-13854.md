---
entity_id: "reaction.ecocyc.RXN-13854"
entity_type: "reaction"
name: "RXN-13854"
source_database: "EcoCyc"
source_id: "RXN-13854"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13854

`reaction.ecocyc.RXN-13854`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13854`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMMONIUM + WATER + NAD -> NITRITE + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: AMMONIUM + WATER + NAD -> NITRITE + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by nitrite reductase - NADH dependent (complex.ecocyc.NITRITREDUCT-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), ammonium (molecule.ecocyc.AMMONIUM). Products: NADH (molecule.C00004), H+ (molecule.C00080), Nitrite (molecule.C00088).

## Annotation

AMMONIUM + WATER + NAD -> NITRITE + NADH + PROTON; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.NITRITREDUCT-CPLX|complex.ecocyc.NITRITREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-13854`

## Notes

AMMONIUM + WATER + NAD -> NITRITE + NADH + PROTON; direction=RIGHT-TO-LEFT
