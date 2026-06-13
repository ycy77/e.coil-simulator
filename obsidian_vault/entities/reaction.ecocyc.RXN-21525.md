---
entity_id: "reaction.ecocyc.RXN-21525"
entity_type: "reaction"
name: "RXN-21525"
source_database: "EcoCyc"
source_id: "RXN-21525"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21525

`reaction.ecocyc.RXN-21525`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21525`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxymethylbilane-Synthase-ES4 + WATER -> HYDROXYMETHYLBILANE + Holo-Hydroxymethylbilane-Synthase; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hydroxymethylbilane-Synthase-ES4 + WATER -> HYDROXYMETHYLBILANE + Holo-Hydroxymethylbilane-Synthase; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a [hydroxymethylbilane synthase] ES4 intermediate (molecule.ecocyc.Hydroxymethylbilane-Synthase-ES4). Products: Hydroxymethylbilane (molecule.C01024), a holo-[hydroxymethylbilane synthase] (molecule.ecocyc.Holo-Hydroxymethylbilane-Synthase).

## Annotation

Hydroxymethylbilane-Synthase-ES4 + WATER -> HYDROXYMETHYLBILANE + Holo-Hydroxymethylbilane-Synthase; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C01024|molecule.C01024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Holo-Hydroxymethylbilane-Synthase|molecule.ecocyc.Holo-Hydroxymethylbilane-Synthase]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydroxymethylbilane-Synthase-ES4|molecule.ecocyc.Hydroxymethylbilane-Synthase-ES4]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21525`

## Notes

Hydroxymethylbilane-Synthase-ES4 + WATER -> HYDROXYMETHYLBILANE + Holo-Hydroxymethylbilane-Synthase; direction=PHYSIOL-LEFT-TO-RIGHT
