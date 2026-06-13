---
entity_id: "reaction.ecocyc.RXN0-6708"
entity_type: "reaction"
name: "RXN0-6708"
source_database: "EcoCyc"
source_id: "RXN0-6708"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6708

`reaction.ecocyc.RXN0-6708`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6708`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD0-2461 + WATER -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD0-2461 + WATER -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cytosine/isoguanine deaminase (complex.ecocyc.CPLX0-7932). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), isoguanine (molecule.ecocyc.CPD0-2461). Products: Xanthine (molecule.C00385), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

PROTON + CPD0-2461 + WATER -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7932|complex.ecocyc.CPLX0-7932]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2461|molecule.ecocyc.CPD0-2461]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6708`

## Notes

PROTON + CPD0-2461 + WATER -> XANTHINE + AMMONIUM; direction=LEFT-TO-RIGHT
