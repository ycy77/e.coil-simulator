---
entity_id: "reaction.ecocyc.RXN0-7349"
entity_type: "reaction"
name: "RXN0-7349"
source_database: "EcoCyc"
source_id: "RXN0-7349"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7349

`reaction.ecocyc.RXN0-7349`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7349`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-uridine34 + OXYGEN-MOLECULE -> 5-HYDROXYU34-TRNA; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-uridine34 + OXYGEN-MOLECULE -> 5-HYDROXYU34-TRNA; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by trhO (protein.P24188). Substrates: Oxygen (molecule.C00007), a uridine34 in tRNA (molecule.ecocyc.tRNA-uridine34). Products: a 5-hydroxyuridine34 in tRNA (molecule.ecocyc.5-HYDROXYU34-TRNA).

## Enriched Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Annotation

tRNA-uridine34 + OXYGEN-MOLECULE -> 5-HYDROXYU34-TRNA; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P24188|protein.P24188]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.5-HYDROXYU34-TRNA|molecule.ecocyc.5-HYDROXYU34-TRNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine34|molecule.ecocyc.tRNA-uridine34]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7349`

## Notes

tRNA-uridine34 + OXYGEN-MOLECULE -> 5-HYDROXYU34-TRNA; direction=PHYSIOL-LEFT-TO-RIGHT
