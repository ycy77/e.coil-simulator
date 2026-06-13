---
entity_id: "reaction.ecocyc.RXN-14139"
entity_type: "reaction"
name: "RXN-14139"
source_database: "EcoCyc"
source_id: "RXN-14139"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14139

`reaction.ecocyc.RXN-14139`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14139`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + WATER -> UMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UTP + WATER -> UMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside triphosphate pyrophosphatase YhdE (complex.ecocyc.CPLX0-8106). Substrates: H2O (molecule.C00001), UTP (molecule.C00075). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), UMP (molecule.C00105).

## Annotation

UTP + WATER -> UMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8106|complex.ecocyc.CPLX0-8106]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14139`

## Notes

UTP + WATER -> UMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
