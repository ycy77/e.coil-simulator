---
entity_id: "reaction.ecocyc.RXN0-7005"
entity_type: "reaction"
name: "RXN0-7005"
source_database: "EcoCyc"
source_id: "RXN0-7005"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7005

`reaction.ecocyc.RXN0-7005`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7005`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The redox potential of the proline / (S)-1-pyrroline-5-carboxylate couple is -0.123V . EcoCyc reaction equation: L-DELTA1-PYRROLINE_5-CARBOXYLATE + E- + PROTON -> PRO; direction=LEFT-TO-RIGHT. The redox potential of the proline / (S)-1-pyrroline-5-carboxylate couple is -0.123V .

## Biological Role

Substrates: H+ (molecule.C00080), (S)-1-Pyrroline-5-carboxylate (molecule.C03912). Products: L-Proline (molecule.C00148).

## Annotation

The redox potential of the proline / (S)-1-pyrroline-5-carboxylate couple is -0.123V .

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03912|molecule.C03912]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7005`

## Notes

L-DELTA1-PYRROLINE_5-CARBOXYLATE + E- + PROTON -> PRO; direction=LEFT-TO-RIGHT
