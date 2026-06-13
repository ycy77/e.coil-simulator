---
entity_id: "reaction.ecocyc.RXN-13248"
entity_type: "reaction"
name: "RXN-13248"
source_database: "EcoCyc"
source_id: "RXN-13248"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13248

`reaction.ecocyc.RXN-13248`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13248`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12642 + PROTON -> Methylketones + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12642 + PROTON -> Methylketones + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a 3-oxoacid (molecule.ecocyc.CPD-12642). Products: CO2 (molecule.C00011), a methyl ketone (molecule.ecocyc.Methylketones).

## Annotation

CPD-12642 + PROTON -> Methylketones + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Methylketones|molecule.ecocyc.Methylketones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12642|molecule.ecocyc.CPD-12642]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13248`

## Notes

CPD-12642 + PROTON -> Methylketones + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
