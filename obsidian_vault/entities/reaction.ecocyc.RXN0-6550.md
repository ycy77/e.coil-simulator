---
entity_id: "reaction.ecocyc.RXN0-6550"
entity_type: "reaction"
name: "RXN0-6550"
source_database: "EcoCyc"
source_id: "RXN0-6550"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6550

`reaction.ecocyc.RXN0-6550`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6550`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CH33ADO + WATER -> 5-Deoxy-D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CH33ADO + WATER -> 5-Deoxy-D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase (complex.ecocyc.CPLX0-1541). Substrates: H2O (molecule.C00001), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO). Products: Adenine (molecule.C00147), 5-deoxy-D-ribofuranose (molecule.ecocyc.5-Deoxy-D-Ribofuranose).

## Annotation

CH33ADO + WATER -> 5-Deoxy-D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1541|complex.ecocyc.CPLX0-1541]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-Deoxy-D-Ribofuranose|molecule.ecocyc.5-Deoxy-D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6550`

## Notes

CH33ADO + WATER -> 5-Deoxy-D-Ribofuranose + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT
