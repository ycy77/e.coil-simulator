---
entity_id: "reaction.ecocyc.OXALODECARB-RXN"
entity_type: "reaction"
name: "OXALODECARB-RXN"
source_database: "EcoCyc"
source_id: "OXALODECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OXALODECARB-RXN

`reaction.ecocyc.OXALODECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OXALODECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the metabolism of glycolate and glyoxalate. EcoCyc reaction equation: PROTON + OXALACETIC_ACID -> PYRUVATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the metabolism of glycolate and glyoxalate.

## Biological Role

Catalyzed by KHG/KDPG aldolase (complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX). Substrates: Oxaloacetate (molecule.C00036), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Pyruvate (molecule.C00022).

## Annotation

This reaction is part of the metabolism of glycolate and glyoxalate.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX|complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OXALODECARB-RXN`

## Notes

PROTON + OXALACETIC_ACID -> PYRUVATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
