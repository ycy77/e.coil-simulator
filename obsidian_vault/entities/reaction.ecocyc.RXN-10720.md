---
entity_id: "reaction.ecocyc.RXN-10720"
entity_type: "reaction"
name: "RXN-10720"
source_database: "EcoCyc"
source_id: "RXN-10720"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10720

`reaction.ecocyc.RXN-10720`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10720`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-476 -> KYNURENATE + WATER + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-476 -> KYNURENATE + WATER + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: 4-(2-Aminophenyl)-2,4-dioxobutanoate (molecule.C01252). Products: H2O (molecule.C00001), H+ (molecule.C00080), 4-Hydroxy-2-quinolinecarboxylic acid (molecule.C01717).

## Annotation

CPD-476 -> KYNURENATE + WATER + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01717|molecule.C01717]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01252|molecule.C01252]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10720`

## Notes

CPD-476 -> KYNURENATE + WATER + PROTON; direction=LEFT-TO-RIGHT
