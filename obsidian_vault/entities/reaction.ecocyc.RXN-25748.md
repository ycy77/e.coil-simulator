---
entity_id: "reaction.ecocyc.RXN-25748"
entity_type: "reaction"
name: "Haber-Weiss reaction"
source_database: "EcoCyc"
source_id: "RXN-25748"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Haber-Weiss reaction

`reaction.ecocyc.RXN-25748`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25748`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROGEN-PEROXIDE + SUPER-OXIDE -> CPD-12377 + OXYGEN-MOLECULE + OH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HYDROGEN-PEROXIDE + SUPER-OXIDE -> CPD-12377 + OXYGEN-MOLECULE + OH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), superoxide (molecule.ecocyc.SUPER-OXIDE). Products: Oxygen (molecule.C00007), hydroxyl radical (molecule.ecocyc.CPD-12377), OH- (molecule.ecocyc.OH).

## Annotation

HYDROGEN-PEROXIDE + SUPER-OXIDE -> CPD-12377 + OXYGEN-MOLECULE + OH; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.OH|molecule.ecocyc.OH]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25748`

## Notes

HYDROGEN-PEROXIDE + SUPER-OXIDE -> CPD-12377 + OXYGEN-MOLECULE + OH; direction=PHYSIOL-LEFT-TO-RIGHT
