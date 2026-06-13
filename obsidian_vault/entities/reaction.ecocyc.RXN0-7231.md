---
entity_id: "reaction.ecocyc.RXN0-7231"
entity_type: "reaction"
name: "RXN0-7231"
source_database: "EcoCyc"
source_id: "RXN0-7231"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7231

`reaction.ecocyc.RXN0-7231`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7231`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETR-Quinones + BETAINE-ALDEHYDE-HYDRATE -> ETR-Quinols + PROTON + BETAINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ETR-Quinones + BETAINE-ALDEHYDE-HYDRATE -> ETR-Quinols + PROTON + BETAINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by betA (protein.P17444). Substrates: betaine aldehyde hydrate (molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE). Products: H+ (molecule.C00080), Betaine (molecule.C00719).

## Annotation

ETR-Quinones + BETAINE-ALDEHYDE-HYDRATE -> ETR-Quinols + PROTON + BETAINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P17444|protein.P17444]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE|molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7231`

## Notes

ETR-Quinones + BETAINE-ALDEHYDE-HYDRATE -> ETR-Quinols + PROTON + BETAINE; direction=PHYSIOL-LEFT-TO-RIGHT
