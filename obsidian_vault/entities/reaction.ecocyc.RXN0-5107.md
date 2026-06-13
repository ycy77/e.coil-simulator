---
entity_id: "reaction.ecocyc.RXN0-5107"
entity_type: "reaction"
name: "RXN0-5107"
source_database: "EcoCyc"
source_id: "RXN0-5107"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5107

`reaction.ecocyc.RXN0-5107`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5107`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TTP + WATER -> PROTON + TMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TTP + WATER -> PROTON + TMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside triphosphate pyrophosphatase YhdE (complex.ecocyc.CPLX0-8106), nudI (protein.P52006). Substrates: H2O (molecule.C00001), dTTP (molecule.C00459). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), dTMP (molecule.C00364).

## Annotation

TTP + WATER -> PROTON + TMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8106|complex.ecocyc.CPLX0-8106]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P52006|protein.P52006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00364|molecule.C00364]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5107`

## Notes

TTP + WATER -> PROTON + TMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
