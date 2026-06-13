---
entity_id: "reaction.ecocyc.RXN-17962"
entity_type: "reaction"
name: "RXN-17962"
source_database: "EcoCyc"
source_id: "RXN-17962"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17962

`reaction.ecocyc.RXN-17962`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17962`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-1106 + ACETYL-COA -> CPD-19243 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-1106 + ACETYL-COA -> CPD-19243 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnO (protein.P16691). Substrates: Acetyl-CoA (molecule.C00024), 2-Aminoethylphosphonate (molecule.C03557). Products: CoA (molecule.C00010), H+ (molecule.C00080), 2-Acetamidoethylphosphonate (molecule.C21403).

## Annotation

CPD-1106 + ACETYL-COA -> CPD-19243 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16691|protein.P16691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21403|molecule.C21403]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03557|molecule.C03557]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17962`

## Notes

CPD-1106 + ACETYL-COA -> CPD-19243 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
