---
entity_id: "reaction.ecocyc.RXN-17960"
entity_type: "reaction"
name: "RXN-17960"
source_database: "EcoCyc"
source_id: "RXN-17960"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17960

`reaction.ecocyc.RXN-17960`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17960`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2521 + ACETYL-COA -> CPD-19240 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2521 + ACETYL-COA -> CPD-19240 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnO (protein.P16691). Substrates: Acetyl-CoA (molecule.C00024), [(S)-1-aminoethyl]phosphonate (molecule.ecocyc.CPD0-2521). Products: CoA (molecule.C00010), H+ (molecule.C00080), [(1S)-1-acetamidoethyl]phosphonate (molecule.ecocyc.CPD-19240).

## Annotation

CPD0-2521 + ACETYL-COA -> CPD-19240 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16691|protein.P16691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19240|molecule.ecocyc.CPD-19240]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2521|molecule.ecocyc.CPD0-2521]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17960`

## Notes

CPD0-2521 + ACETYL-COA -> CPD-19240 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
