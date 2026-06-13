---
entity_id: "reaction.ecocyc.CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN"
entity_type: "reaction"
name: "CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN"
source_database: "EcoCyc"
source_id: "CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN

`reaction.ecocyc.CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CITRATE-LYASE + WATER -> HOLO-CITRATE-LYASE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CITRATE-LYASE + WATER -> HOLO-CITRATE-LYASE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001). Products: Acetate (molecule.C00033), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Annotation

CITRATE-LYASE + WATER -> HOLO-CITRATE-LYASE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CITRATE-PRO-3S-LYASE-THIOLESTERASE-RXN`

## Notes

CITRATE-LYASE + WATER -> HOLO-CITRATE-LYASE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
