---
entity_id: "reaction.ecocyc.RXN-14064"
entity_type: "reaction"
name: "RXN-14064"
source_database: "EcoCyc"
source_id: "RXN-14064"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14064

`reaction.ecocyc.RXN-14064`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14064`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3709 + WATER -> CPD-3708 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3709 + WATER -> CPD-3708 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cpdB (protein.P08331). Substrates: H2O (molecule.C00001), 2',3'-Cyclic GMP (molecule.C06194). Products: H+ (molecule.C00080), Guanosine 3'-phosphate (molecule.C06193).

## Annotation

CPD-3709 + WATER -> CPD-3708 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P08331|protein.P08331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06193|molecule.C06193]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06194|molecule.C06194]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14064`

## Notes

CPD-3709 + WATER -> CPD-3708 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
