---
entity_id: "reaction.ecocyc.RXN-12895"
entity_type: "reaction"
name: "RXN-12895"
source_database: "EcoCyc"
source_id: "RXN-12895"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12895

`reaction.ecocyc.RXN-12895`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12895`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22331 + WATER + PROTON -> CPD-22332 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-22331 + WATER + PROTON -> CPD-22332 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), (Z)-2-methylureidoacrylate (molecule.ecocyc.CPD-22331). Products: CO2 (molecule.C00011), ammonium (molecule.ecocyc.AMMONIUM), (Z)-2-methylaminoacrylate (molecule.ecocyc.CPD-22332).

## Annotation

CPD-22331 + WATER + PROTON -> CPD-22332 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22332|molecule.ecocyc.CPD-22332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22331|molecule.ecocyc.CPD-22331]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12895`

## Notes

CPD-22331 + WATER + PROTON -> CPD-22332 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
