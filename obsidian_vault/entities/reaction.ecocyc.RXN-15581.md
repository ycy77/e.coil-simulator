---
entity_id: "reaction.ecocyc.RXN-15581"
entity_type: "reaction"
name: "RXN-15581"
source_database: "EcoCyc"
source_id: "RXN-15581"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15581

`reaction.ecocyc.RXN-15581`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15581`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-SERINE -> 2-AMINOACRYLATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-SERINE -> 2-AMINOACRYLATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: D-Serine (molecule.C00740). Products: H2O (molecule.C00001), Dehydroalanine (molecule.C02218).

## Enriched Pathways

- `ecocyc.PWY0-1535` D-serine degradation (EcoCyc)

## Annotation

D-SERINE -> 2-AMINOACRYLATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1535` D-serine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15581`

## Notes

D-SERINE -> 2-AMINOACRYLATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
