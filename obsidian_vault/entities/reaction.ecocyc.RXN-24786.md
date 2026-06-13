---
entity_id: "reaction.ecocyc.RXN-24786"
entity_type: "reaction"
name: "RXN-24786"
source_database: "EcoCyc"
source_id: "RXN-24786"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24786

`reaction.ecocyc.RXN-24786`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24786`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-AMINO-BUTYRATE + CARBON-DIOXIDE -> CPD-27332 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 4-AMINO-BUTYRATE + CARBON-DIOXIDE -> CPD-27332 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: CO2 (molecule.C00011), 4-Aminobutanoate (molecule.C00334). Products: H+ (molecule.C00080), 4-(carboxyamino)butanoate (molecule.ecocyc.CPD-27332).

## Annotation

4-AMINO-BUTYRATE + CARBON-DIOXIDE -> CPD-27332 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-27332|molecule.ecocyc.CPD-27332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24786`

## Notes

4-AMINO-BUTYRATE + CARBON-DIOXIDE -> CPD-27332 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
