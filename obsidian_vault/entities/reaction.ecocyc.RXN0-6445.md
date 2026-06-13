---
entity_id: "reaction.ecocyc.RXN0-6445"
entity_type: "reaction"
name: "RXN0-6445"
source_database: "EcoCyc"
source_id: "RXN0-6445"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6445

`reaction.ecocyc.RXN0-6445`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6445`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MONOMER0-4170 + NAD + WATER -> CHEY-MONOMER + CPD-14762 + NIACINAMIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MONOMER0-4170 + NAD + WATER -> CHEY-MONOMER + CPD-14762 + NIACINAMIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein-lysine deacetylase/desuccinylase/delipoylase (complex.ecocyc.CPLX0-8550). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003). Products: Nicotinamide (molecule.C00153), 2''-O-acetyl-ADP-ribose (molecule.ecocyc.CPD-14762).

## Annotation

MONOMER0-4170 + NAD + WATER -> CHEY-MONOMER + CPD-14762 + NIACINAMIDE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8550|complex.ecocyc.CPLX0-8550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14762|molecule.ecocyc.CPD-14762]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6445`

## Notes

MONOMER0-4170 + NAD + WATER -> CHEY-MONOMER + CPD-14762 + NIACINAMIDE; direction=LEFT-TO-RIGHT
