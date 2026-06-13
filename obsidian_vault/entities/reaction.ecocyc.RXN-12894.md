---
entity_id: "reaction.ecocyc.RXN-12894"
entity_type: "reaction"
name: "RXN-12894"
source_database: "EcoCyc"
source_id: "RXN-12894"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12894

`reaction.ecocyc.RXN-12894`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12894`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2331 + WATER + PROTON -> CPD0-2339 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2331 + WATER + PROTON -> CPD0-2339 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Ureidoacrylate (molecule.C20254). Products: CO2 (molecule.C00011), Aminoacrylate (molecule.C20253), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

CPD0-2331 + WATER + PROTON -> CPD0-2339 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20253|molecule.C20253]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20254|molecule.C20254]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12894`

## Notes

CPD0-2331 + WATER + PROTON -> CPD0-2339 + AMMONIUM + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
