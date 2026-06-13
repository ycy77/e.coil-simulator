---
entity_id: "reaction.ecocyc.RXN-14196"
entity_type: "reaction"
name: "RXN-14196"
source_database: "EcoCyc"
source_id: "RXN-14196"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14196

`reaction.ecocyc.RXN-14196`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14196`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARBAMATE + ATP -> CARBAMOYL-P + ADP; direction=REVERSIBLE EcoCyc reaction equation: CARBAMATE + ATP -> CARBAMOYL-P + ADP; direction=REVERSIBLE.

## Biological Role

Substrates: ATP (molecule.C00002), Carbamate (molecule.C01563). Products: ADP (molecule.C00008), Carbamoyl phosphate (molecule.C00169).

## Enriched Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Annotation

CARBAMATE + ATP -> CARBAMOYL-P + ADP; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14196`

## Notes

CARBAMATE + ATP -> CARBAMOYL-P + ADP; direction=REVERSIBLE
