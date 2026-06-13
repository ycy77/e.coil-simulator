---
entity_id: "reaction.ecocyc.RXN-12541"
entity_type: "reaction"
name: "RXN-12541"
source_database: "EcoCyc"
source_id: "RXN-12541"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12541

`reaction.ecocyc.RXN-12541`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12541`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SUPER-OXIDE + FE+3 -> OXYGEN-MOLECULE + FE+2; direction=REVERSIBLE EcoCyc reaction equation: SUPER-OXIDE + FE+3 -> OXYGEN-MOLECULE + FE+2; direction=REVERSIBLE.

## Biological Role

Substrates: Fe3+ (molecule.C14819), superoxide (molecule.ecocyc.SUPER-OXIDE). Products: Oxygen (molecule.C00007), Fe2+ (molecule.C14818).

## Annotation

SUPER-OXIDE + FE+3 -> OXYGEN-MOLECULE + FE+2; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12541`

## Notes

SUPER-OXIDE + FE+3 -> OXYGEN-MOLECULE + FE+2; direction=REVERSIBLE
