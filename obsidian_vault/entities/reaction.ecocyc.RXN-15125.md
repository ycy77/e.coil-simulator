---
entity_id: "reaction.ecocyc.RXN-15125"
entity_type: "reaction"
name: "RXN-15125"
source_database: "EcoCyc"
source_id: "RXN-15125"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15125

`reaction.ecocyc.RXN-15125`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15125`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SER -> 2-AMINOACRYLATE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: SER -> 2-AMINOACRYLATE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Serine (molecule.C00065). Products: H2O (molecule.C00001), Dehydroalanine (molecule.C02218).

## Enriched Pathways

- `ecocyc.SERDEG-PWY` L-serine degradation (EcoCyc)

## Annotation

SER -> 2-AMINOACRYLATE + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.SERDEG-PWY` L-serine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15125`

## Notes

SER -> 2-AMINOACRYLATE + WATER; direction=LEFT-TO-RIGHT
