---
entity_id: "reaction.ecocyc.RXN0-7426"
entity_type: "reaction"
name: "RXN0-7426"
source_database: "EcoCyc"
source_id: "RXN0-7426"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7426

`reaction.ecocyc.RXN0-7426`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7426`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ferric-Hydroxamate-Complexes + Donor-H1 -> Hydroxamate-siderophores + Acceptor + FE+2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ferric-Hydroxamate-Complexes + Donor-H1 -> Hydroxamate-siderophores + Acceptor + FE+2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fhuF (protein.P39405). Substrates: a ferric hydroxamate complex (molecule.ecocyc.Ferric-Hydroxamate-Complexes). Products: Fe2+ (molecule.C14818), a hydroxamate siderophore (molecule.ecocyc.Hydroxamate-siderophores).

## Annotation

Ferric-Hydroxamate-Complexes + Donor-H1 -> Hydroxamate-siderophores + Acceptor + FE+2; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P39405|protein.P39405]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hydroxamate-siderophores|molecule.ecocyc.Hydroxamate-siderophores]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Ferric-Hydroxamate-Complexes|molecule.ecocyc.Ferric-Hydroxamate-Complexes]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7426`

## Notes

Ferric-Hydroxamate-Complexes + Donor-H1 -> Hydroxamate-siderophores + Acceptor + FE+2; direction=PHYSIOL-LEFT-TO-RIGHT
