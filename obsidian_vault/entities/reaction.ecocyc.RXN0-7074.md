---
entity_id: "reaction.ecocyc.RXN0-7074"
entity_type: "reaction"
name: "RXN0-7074"
source_database: "EcoCyc"
source_id: "RXN0-7074"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7074

`reaction.ecocyc.RXN0-7074`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7074`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRIDOXAMINE-5P + Deaminated-Amine-Donors -> PYRIDOXAL_PHOSPHATE + Aminated-Amine-Donors; direction=REVERSIBLE EcoCyc reaction equation: PYRIDOXAMINE-5P + Deaminated-Amine-Donors -> PYRIDOXAL_PHOSPHATE + Aminated-Amine-Donors; direction=REVERSIBLE.

## Biological Role

Catalyzed by PYRDAMPTRANS-MONOMER (protein.ecocyc.PYRDAMPTRANS-MONOMER). Substrates: Pyridoxamine phosphate (molecule.C00647), a deaminated amino group donor (molecule.ecocyc.Deaminated-Amine-Donors). Products: Pyridoxal phosphate (molecule.C00018), an aminated amino group donor (molecule.ecocyc.Aminated-Amine-Donors).

## Annotation

PYRIDOXAMINE-5P + Deaminated-Amine-Donors -> PYRIDOXAL_PHOSPHATE + Aminated-Amine-Donors; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.ecocyc.PYRDAMPTRANS-MONOMER|protein.ecocyc.PYRDAMPTRANS-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aminated-Amine-Donors|molecule.ecocyc.Aminated-Amine-Donors]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00647|molecule.C00647]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Deaminated-Amine-Donors|molecule.ecocyc.Deaminated-Amine-Donors]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7074`

## Notes

PYRIDOXAMINE-5P + Deaminated-Amine-Donors -> PYRIDOXAL_PHOSPHATE + Aminated-Amine-Donors; direction=REVERSIBLE
