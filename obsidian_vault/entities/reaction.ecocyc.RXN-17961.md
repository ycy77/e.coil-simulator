---
entity_id: "reaction.ecocyc.RXN-17961"
entity_type: "reaction"
name: "RXN-17961"
source_database: "EcoCyc"
source_id: "RXN-17961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17961

`reaction.ecocyc.RXN-17961`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19241 + ACETYL-COA -> CPD-19242 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-19241 + ACETYL-COA -> CPD-19242 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnO (protein.P16691). Substrates: Acetyl-CoA (molecule.C00024), [(R)-1-aminoethyl]phosphonate (molecule.ecocyc.CPD-19241). Products: CoA (molecule.C00010), H+ (molecule.C00080), [(1R)-1-acetamidoethyl]phosphonate (molecule.ecocyc.CPD-19242).

## Annotation

CPD-19241 + ACETYL-COA -> CPD-19242 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16691|protein.P16691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19242|molecule.ecocyc.CPD-19242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19241|molecule.ecocyc.CPD-19241]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17961`

## Notes

CPD-19241 + ACETYL-COA -> CPD-19242 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
