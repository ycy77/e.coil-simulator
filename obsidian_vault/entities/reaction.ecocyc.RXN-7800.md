---
entity_id: "reaction.ecocyc.RXN-7800"
entity_type: "reaction"
name: "RXN-7800"
source_database: "EcoCyc"
source_id: "RXN-7800"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7800

`reaction.ecocyc.RXN-7800`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7800`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD-7100 -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-7100 -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), (2S)-2-Isopropyl-3-oxosuccinate (molecule.C04236). Products: CO2 (molecule.C00011), 4-Methyl-2-oxopentanoate (molecule.C00233).

## Enriched Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Annotation

PROTON + CPD-7100 -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00233|molecule.C00233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04236|molecule.C04236]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7800`

## Notes

PROTON + CPD-7100 -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
