---
entity_id: "reaction.ecocyc.RXN0-7078"
entity_type: "reaction"
name: "RXN0-7078"
source_database: "EcoCyc"
source_id: "RXN0-7078"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7078

`reaction.ecocyc.RXN0-7078`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7078`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD3O-0 + NAD + WATER -> Protein-L-lysine + CPD-14762 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD3O-0 + NAD + WATER -> Protein-L-lysine + CPD-14762 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein-lysine deacetylase/desuccinylase/delipoylase (complex.ecocyc.CPLX0-8550). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), a [protein]-N6-acetyl-L-lysine (molecule.ecocyc.CPD3O-0). Products: Nicotinamide (molecule.C00153), Protein lysine (molecule.C02188), 2''-O-acetyl-ADP-ribose (molecule.ecocyc.CPD-14762).

## Annotation

CPD3O-0 + NAD + WATER -> Protein-L-lysine + CPD-14762 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8550|complex.ecocyc.CPLX0-8550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14762|molecule.ecocyc.CPD-14762]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD3O-0|molecule.ecocyc.CPD3O-0]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7078`

## Notes

CPD3O-0 + NAD + WATER -> Protein-L-lysine + CPD-14762 + NIACINAMIDE; direction=PHYSIOL-LEFT-TO-RIGHT
