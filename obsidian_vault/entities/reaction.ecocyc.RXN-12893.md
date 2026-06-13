---
entity_id: "reaction.ecocyc.RXN-12893"
entity_type: "reaction"
name: "RXN-12893"
source_database: "EcoCyc"
source_id: "RXN-12893"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12893

`reaction.ecocyc.RXN-12893`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12893`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-69 + HCO3 + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-69 + HCO3 + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), HCO3- (molecule.C00288), Cyanate (molecule.C01417). Products: CO2 (molecule.C00011), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

CPD-69 + HCO3 + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12893`

## Notes

CPD-69 + HCO3 + PROTON -> AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
