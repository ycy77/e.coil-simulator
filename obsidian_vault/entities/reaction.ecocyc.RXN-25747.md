---
entity_id: "reaction.ecocyc.RXN-25747"
entity_type: "reaction"
name: "Haber-Weiss cycle"
source_database: "EcoCyc"
source_id: "RXN-25747"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Haber-Weiss cycle

`reaction.ecocyc.RXN-25747`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25747`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12377 + HYDROGEN-PEROXIDE -> WATER + SUPER-OXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12377 + HYDROGEN-PEROXIDE -> WATER + SUPER-OXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), H+ (molecule.C00080), superoxide (molecule.ecocyc.SUPER-OXIDE).

## Annotation

CPD-12377 + HYDROGEN-PEROXIDE -> WATER + SUPER-OXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25747`

## Notes

CPD-12377 + HYDROGEN-PEROXIDE -> WATER + SUPER-OXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
